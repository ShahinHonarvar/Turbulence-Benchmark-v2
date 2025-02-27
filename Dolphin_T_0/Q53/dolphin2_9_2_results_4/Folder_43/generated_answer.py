def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    for i in range(len(s)):
        for j in range(i + 48, len(s)):
            subs = s[i:j + 1]
            if subs == subs[::-1] and subs.isalpha():
                pals.add(subs[::-1])
    return pals