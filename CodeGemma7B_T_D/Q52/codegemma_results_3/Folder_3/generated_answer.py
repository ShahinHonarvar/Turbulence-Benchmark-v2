def palindrome_of_length_n(my_str):
    a, b = (0, len(my_str) - 1)
    ans = set()
    while b - a + 1 < 100 and b >= a:
        s = my_str[a:b + 1]
        if len(s) == 100 and s == s[::-1]:
            ans.add(s)
        if s[0].lower() > s[a].lower():
            b -= 1
        elif s[-1].lower() < s[b].lower():
            a += 1
        else:
            a += 1
            b -= 1
    return ans