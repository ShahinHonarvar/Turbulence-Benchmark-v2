def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    letters_between_indices = {char.lower() for char in s[2:10] if char.isalpha()}
    for letter in letters_between_indices:
        if letters_between_indices.count(letter) >= 2:
            palindromes.add(letter * 2)
    return palindromes