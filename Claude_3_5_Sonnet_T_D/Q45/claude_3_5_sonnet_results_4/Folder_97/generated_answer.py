def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[:5] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        palindromes = set()
        for perm in __import__('itertools').permutations(chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
        return palindromes
    all_palindromes = set()
    for length in range(3, len(letters) + 1):
        all_palindromes.update(generate_palindromes(letters, length))
    return all_palindromes