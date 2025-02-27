def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    n = 51
    len_s = len(s)
    for pal_len in range(n, len_s + 1):
        for i in range(0, len_s - pal_len + 1):
            pal = s[i:i + pal_len]
            if pal == pal[::-1]:
                pals.add(pal)
    return pals