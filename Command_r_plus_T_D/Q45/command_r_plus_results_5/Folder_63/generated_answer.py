def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[:4])
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            substring = english_letters[i:j]
            for palindrome in substring.split():
                if is_palindrome(palindrome) and len(palindrome) >= 3:
                    all_palindromes.add(palindrome)
    return all_palindromes