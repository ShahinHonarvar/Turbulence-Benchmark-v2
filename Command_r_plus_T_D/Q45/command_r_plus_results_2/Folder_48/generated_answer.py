def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = [char for char in s[6:9] if char.isalpha()]
    if len(english_letters) >= 2:
        for i in range(len(english_letters)):
            for j in range(i + 1, len(english_letters)):
                palindrome = english_letters[i] + english_letters[j] + english_letters[j] + english_letters[i]
                palindromes.add(palindrome.lower())
    return palindromes