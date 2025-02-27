def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:5].lower())
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if is_palindrome(word) and len(word) >= 4:
            palindromes.add(word)
    return palindromes