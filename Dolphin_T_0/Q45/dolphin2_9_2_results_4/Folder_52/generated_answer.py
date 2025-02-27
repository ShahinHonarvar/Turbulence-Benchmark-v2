def palindromes_between_indices(string):
    string = string[:8]
    string = ''.join(filter(str.isalpha, string)).lower()
    if len(set(string)) < 6:
        return set()
    palindromes = set()
    for word in itertools.permutations(string, 6):
        word = ''.join(word)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes