def palindrome_of_length_at_least_n(s):
    ans = set()
    for i in range(len(s)):
        for j in range(i + 1, min(i + 64, len(s)) + 1):
            if s[i:j] == s[i:j][::-1]:
                ans.add(s[i:j])
    return ans