def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 100
    pals = set()
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if subs == subs[::-1] and subs.isalpha():
            pals.add(subs)
    return pals