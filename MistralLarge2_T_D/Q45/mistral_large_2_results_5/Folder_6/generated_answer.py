import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes