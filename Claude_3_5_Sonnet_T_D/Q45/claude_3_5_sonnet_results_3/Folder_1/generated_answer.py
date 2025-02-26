def palindromes_between_indices(string):
    letters = ''.join((char.lower() for char in string[4:8] if char.isalpha()))

    def generate_palindromes(chars, min_length):
        result = set()
        for length in range(min_length, len(chars) + 1):
            for i in range(len(chars) - length + 1):
                substring = chars[i:i + length]
                if substring == substring[::-1]:
                    result.add(substring)
        return result

    def generate_permutations(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, char in enumerate(chars):
            for perm in generate_permutations(chars[:i] + chars[i + 1:]):
                result.add(char + perm)
        return result
    all_permutations = generate_permutations(letters)
    palindromes = set()
    for perm in all_permutations:
        palindromes.update(generate_palindromes(perm, 5))
    return palindromes