def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s.upper() if c.isalpha()))
    result_set = set()
    for i in range(len(s)):
        for j in range(len(s), i - 1, -1):
            if len(s[i:j]) >= 93 and s[i:j] == s[i:j][::-1]:
                result_set.add(s[i:j])
    return result_set