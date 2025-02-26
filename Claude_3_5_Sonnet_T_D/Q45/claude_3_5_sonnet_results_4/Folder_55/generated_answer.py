def palindromes_between_indices(s):
    alphabet = ''.join(filter(str.isalpha, s[:3].lower()))

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        result = set()
        for perm in __import__('itertools').permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
        return result
    palindromes = set()
    for length in range(3, len(alphabet) + 1):
        palindromes.update(generate_palindromes(alphabet, length))
    return palindromes