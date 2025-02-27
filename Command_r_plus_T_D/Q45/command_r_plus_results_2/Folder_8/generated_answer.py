def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    letters_between_indices = set(s[1:6].lower())
    for letter in letters_between_indices:
        if letters_between_indices.count(letter) >= 2:
            palindrome = letter * 5
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes