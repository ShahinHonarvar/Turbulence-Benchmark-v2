def palindromes_of_specific_lengths(s):
    s = s[:7]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    len_set = set()
    for length in range(3, 7):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                len_set.add(s[i:i + length])
    return len_set