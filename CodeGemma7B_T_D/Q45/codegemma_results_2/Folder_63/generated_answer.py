def palindromes_between_indices(s):
    chars = set(s)
    if len(chars) < 3:
        return set()
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    filtered_set = alphabets.intersection(chars)
    if not filtered_set:
        return set()
    palindromes = set()
    for word in itertools.permutations(filtered_set):
        word = ''.join(word)
        for i in range(len(word) - 2):
            if word[i] == word[i + 1] and word[i] == word[i + 2]:
                palindromes.add(word)
    return palindromes