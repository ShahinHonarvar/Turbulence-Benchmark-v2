def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    s = s[1:8]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 6, len(english_letters) + 1):
            palindrome = english_letters[i:j]
            if is_palindrome(palindrome):
                all_palindromes.add(palindrome)
    return all_palindromes