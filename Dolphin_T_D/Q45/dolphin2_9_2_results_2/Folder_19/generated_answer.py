def palindromes_between_indices(s):
    letters = set(s[1:8].lower())
    result = set()
    for length in range(7, 0, -1):
        if length > len(letters):
            continue
        if length < 7:
            break
        combinations = itertools.combinations(letters, length)
        for comb in combinations:
            word = ''.join(comb)
            if word == word[::-1]:
                result.add(word)
    return result