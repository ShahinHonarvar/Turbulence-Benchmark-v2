def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    input_string = input_string.lower()
    english_letters = get_english_letters(input_string[4:10])
    all_palindromes = set()
    for i in range(5, len(english_letters) + 1):
        for j in range(len(english_letters) - i + 1):
            palindrome = english_letters[j:j + i]
            if is_palindrome(palindrome):
                all_palindromes.add(palindrome)
    return all_palindromes