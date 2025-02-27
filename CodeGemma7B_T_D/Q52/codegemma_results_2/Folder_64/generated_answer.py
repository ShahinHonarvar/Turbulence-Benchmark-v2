def palindrome_of_length_n(s):
    ans = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j].lower() == s[i:j][::-1].lower() and len(s[i:j]) == 9:
                ans.add(s[i:j])
    return ans