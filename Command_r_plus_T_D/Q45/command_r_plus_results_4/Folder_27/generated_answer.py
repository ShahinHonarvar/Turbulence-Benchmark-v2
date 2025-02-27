def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            substring = input_string[i:j]
            english_letters = ''.join(filter(str.isalpha, substring)).lower()
            if len(english_letters) >= 6 and is_palindrome(english_letters):
                palindromes.add(english_letters)
    return palindromes