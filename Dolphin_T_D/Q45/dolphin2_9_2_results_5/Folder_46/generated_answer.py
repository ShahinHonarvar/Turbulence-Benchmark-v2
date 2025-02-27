def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            sub_set = set(sub)
            if len(sub_set) == 1 and len(sub) >= 6:
                palindromes.add(sub[0].upper() * len(sub))
            elif len(sub_set) == 2:
                pairs = [c * sub.count(c) for c in sub_set]
                if pairs in zip(sub_set, sub_set):
                    palindromes.add(''.join(pairs))
    return palindromes