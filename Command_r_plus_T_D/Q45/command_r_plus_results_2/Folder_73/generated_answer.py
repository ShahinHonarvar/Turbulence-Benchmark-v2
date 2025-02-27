def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = [char for char in s[3:7] if char.isalpha()]
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring).lower())
    return palindromes