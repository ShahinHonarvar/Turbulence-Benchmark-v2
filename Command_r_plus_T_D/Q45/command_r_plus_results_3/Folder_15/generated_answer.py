def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    unique_letters = set(s[1:3].lower())
    palindromes = set()
    if unique_letters.issubset(english_letters):
        for letter in unique_letters:
            if s[1:3].lower().count(letter) > 1:
                palindromes.add(letter * 2)
            if s[1:3].lower().count(letter) == 2:
                palindromes.add(letter + letter)
    return {p for p in palindromes if is_palindrome(p)}