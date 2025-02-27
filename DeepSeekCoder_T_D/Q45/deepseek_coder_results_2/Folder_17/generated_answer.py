def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:7].lower())
    palindromes = set()
    for combo in permutations(letters, len(letters)):
        word = ''.join(combo)
        if len(word) >= 4 and is_palindrome(word):
            palindromes.add(word)
    return palindromes