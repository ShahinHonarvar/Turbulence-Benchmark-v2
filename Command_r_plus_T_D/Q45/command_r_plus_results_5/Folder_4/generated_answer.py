def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[3:10])
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 7, len(english_letters) + 1):
            sub_string = english_letters[i:j]
            if is_palindrome(sub_string):
                all_palindromes.add(sub_string)
    return all_palindromes