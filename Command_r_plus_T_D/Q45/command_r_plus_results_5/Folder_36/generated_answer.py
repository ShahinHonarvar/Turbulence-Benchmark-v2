def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[5:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring_letters = set(substring) & english_letters
    for letter in substring_letters:
        if substring.count(letter) >= 2:
            palindrome = letter * 2
            palindromes.add(palindrome)
    return palindromes