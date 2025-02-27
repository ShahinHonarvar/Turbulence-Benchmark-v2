def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[1:8].lower()
    letters_in_range = set(s_lower) & english_letters
    for letter in letters_in_range:
        if s_lower.count(letter) >= 2:
            palindrome = letter * 7
            palindromes.add(palindrome)
    return palindromes