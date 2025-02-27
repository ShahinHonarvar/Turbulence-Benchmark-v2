def palindrome_of_length_n(s):
    s = s.lower()
    ans = set()
    n = len(s)
    if n < 47:
        return ans
    for i in range(n - 46):
        for j in range(i + 46, n):
            if s[i:j + 1] == s[j:i - 1:-1]:
                ans.add(s[i:j + 1])
    return ans