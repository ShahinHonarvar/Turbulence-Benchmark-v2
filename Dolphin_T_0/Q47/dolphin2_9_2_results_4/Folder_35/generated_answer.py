def palindromes_of_specific_lengths(s):
    s = s[33:91]
    R = set()
    for L in range(14, 39 + 1):
        for i in range(0, len(s)):
            if i + L <= len(s):
                sub = s[i:i + L]
                if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in sub.lower())) and sub.lower() == sub.lower()[::-1]:
                    R.add(sub)
    return R