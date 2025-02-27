def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    for length in range(27, len(s) + 1):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1]:
                pals.add(subs)
    return pals