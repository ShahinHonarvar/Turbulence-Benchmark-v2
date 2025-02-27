def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(string: str) -> str:
        return ''.join((char for char in string if char.isalpha())).lower()
    english_letters = get_english_letters(input_string[1:4])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            sub_string = english_letters[i:j]
            if is_palindrome(sub_string) and len(sub_string) >= 4:
                palindromes.add(sub_string)
    return palindromes