def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(string: str) -> str:
        return ''.join((char for char in string if char.isalpha())).lower()
    input_string = input_string[:7]
    english_letters = get_english_letters(input_string)
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 5, len(english_letters) + 1):
            sub_string = english_letters[i:j]
            if is_palindrome(sub_string):
                palindromes.add(sub_string)
    return palindromes