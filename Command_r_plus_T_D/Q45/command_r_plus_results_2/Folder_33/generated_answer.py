def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(7, min(len(s), 10)):
        substring = s[7:i + 1]
        substring_lower = substring.lower()
        if all((char in english_letters for char in substring_lower)):
            if substring_lower == substring_lower[::-1] and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes