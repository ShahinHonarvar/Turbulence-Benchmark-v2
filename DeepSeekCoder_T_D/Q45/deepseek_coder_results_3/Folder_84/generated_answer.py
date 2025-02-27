def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:10].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                palindrome = letter1 + letter2 + letter3
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes