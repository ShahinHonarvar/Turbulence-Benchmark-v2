def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7].lower()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= len(chars):
            for perm in __import__('itertools').permutations(chars, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    yield word
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes