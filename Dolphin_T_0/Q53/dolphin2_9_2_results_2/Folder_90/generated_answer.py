def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_res = set()
    for i in range(len(s)):
        for j in range(140, len(s) - i + 1):
            if s[i:i + j] == s[i:i + j][::-1]:
                set_res.add(s[i:i + j])
    return set_res