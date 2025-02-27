def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:8].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    for letter5 in letters:
                        word = letter1 + letter2 + letter3 + letter4 + letter5
                        if is_palindrome(word):
                            palindromes.add(word)
    return palindromes