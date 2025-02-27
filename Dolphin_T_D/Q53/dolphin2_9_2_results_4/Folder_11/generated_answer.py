def palindrome_of_length_at_least_n(s):
    s = s.lower()
    out = set()
    for i in range(len(s) - 53):
        for j in range(i + 54, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                out.add(subs)
    return out