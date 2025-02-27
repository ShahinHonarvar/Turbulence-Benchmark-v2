def palindromes_between_indices(string):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    if len(string) < 6:
        return set()
    english_letters = string[:7]
    english_letters = ''.join(sorted(english_letters))
    result = set()
    for i in range(4, len(english_letters) + 1):
        for word in combinations(english_letters, i):
            word = ''.join(word)
            if is_palindrome(word):
                result.add(word)
    return result