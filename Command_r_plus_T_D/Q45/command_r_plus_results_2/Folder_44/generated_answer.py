def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[2:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring_letters = set(substring) & english_letters
    for letter in substring_letters:
        if substring.count(letter) >= 2:
            palindromes.add(letter * 2)
    for i in range(len(substring) - 1):
        if substring[i] == substring[i + 1]:
            palindromes.add(substring[i:i + 2])
    return palindromes