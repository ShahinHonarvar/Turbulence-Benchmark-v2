def palindromes_between_indices(s):
    s = s[4:9].lower()
    if len(s) < 4:
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and len(subs) >= 4:
                palindromes.add(subs)
    return palindromes