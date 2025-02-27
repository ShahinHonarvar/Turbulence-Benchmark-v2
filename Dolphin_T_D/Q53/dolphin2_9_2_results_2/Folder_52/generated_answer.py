def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    for i in range(14, len(s) + 1):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            if subs == subs[::-1]:
                pals.add(subs)
    return pals