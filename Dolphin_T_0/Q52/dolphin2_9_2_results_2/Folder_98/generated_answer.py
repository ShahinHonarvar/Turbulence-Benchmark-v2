def palindrome_of_length_n(s):
    s = s.lower()
    ans = set()
    for i in range(len(s) - 5):
        subs = s[i:i + 6]
        if subs == subs[::-1] and subs.isalpha():
            ans.add(subs)
    return ans