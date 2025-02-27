def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[5:9].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                word = letter1 + letter2 + letter3
                if is_palindrome(word):
                    palindromes.add(word)
    return {p for p in palindromes if len(p) >= 3}