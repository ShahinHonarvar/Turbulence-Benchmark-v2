import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            word = ''.join(combination)
            if is_palindrome(word):
                unique_palindromes.add(word)
    return unique_palindromes