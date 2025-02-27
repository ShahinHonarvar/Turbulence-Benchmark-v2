def palindrome_of_length_at_least_n(s):
    s = s.lower()
    k = 22
    ret = set()
    for i in range(len(s)):
        for j in range(i + k, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                ret.add(s[i:j])
    return ret