def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:9].lower())
    palindromes = set()
    for letter in letters:
        for letter2 in letters:
            for letter3 in letters:
                if letter != letter2 and letter != letter3 and (letter2 != letter3):
                    word = letter + letter2 + letter3
                    if is_palindrome(word):
                        palindromes.add(word)
    return palindromes