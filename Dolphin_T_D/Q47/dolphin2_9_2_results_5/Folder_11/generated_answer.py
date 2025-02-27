def palindromes_of_specific_lengths(s):
    s = s[23:97]
    out = set()
    for length in range(10, 37):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs.lower()[::-1] and subs.isalpha():
                out.add(subs)
    return out