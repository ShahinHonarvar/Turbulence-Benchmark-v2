def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[:7])
    if len(english_letters) < 7:
        return set()
    all_palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 1, len(english_letters) - 5):
            substring = english_letters[i:j] + english_letters[j + 1:i - ~j]
            for palindrome in substring + substring[::-1]:
                if len(palindrome) >= 7 and is_palindrome(palindrome):
                    all_palindromes.add(palindrome)
    return all_palindromes