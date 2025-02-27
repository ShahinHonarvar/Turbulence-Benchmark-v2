def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[5:10].lower()
    letters_in_range = set(substring) & english_letters
    for letter in letters_in_range:
        count = substring.count(letter)
        if count >= 3:
            palindromes.add(letter * count)
        if count >= 2:
            for other_letter in letters_in_range - {letter}:
                palindromes.add(letter * (count - 1) + other_letter * 2)
    for palindrome in palindromes:
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes