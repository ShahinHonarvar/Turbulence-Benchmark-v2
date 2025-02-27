def palindromes_between_indices(s):
    alphabets = [x for x in s[2:9] if x.lower() in string.ascii_lowercase]
    permutations = set(itertools.permutations(alphabets))
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if len(word) >= 4 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes