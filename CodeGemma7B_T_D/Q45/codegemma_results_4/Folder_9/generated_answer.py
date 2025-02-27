def palindromes_between_indices(s):
    small_letters = frozenset(string.ascii_lowercase)
    d = defaultdict(list)
    palindromes = set()
    for i in range(len(s)):
        if s[i].lower() in small_letters:
            d[s[i].lower()].append(i)
    for i in range(len(s) - 7):
        for l in d:
            indexes = d[l]
            for j in range(len(indexes)):
                for k in range(j + 1, len(indexes)):
                    if indexes[j] >= i and indexes[j] <= i + 7 and (indexes[k] >= i) and (indexes[k] <= i + 7):
                        sub_s = ''.join(sorted([l] * (indexes[k] - indexes[j] + 1)))
                        palindromes.add(sub_s)
    return palindromes