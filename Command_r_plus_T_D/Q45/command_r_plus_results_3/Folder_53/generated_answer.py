def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    input_string = input_string.lower()
    english_letters = get_english_letters(input_string[4:9])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 6, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes