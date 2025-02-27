def palindrome_of_length_n(s):
    s = s.lower()
    n = 97
    pals = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                pals.add(subs)
    return pals