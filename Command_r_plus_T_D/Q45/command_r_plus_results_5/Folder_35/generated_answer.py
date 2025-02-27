def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for i in range(2, 5):
        char = input_string[i]
        if char.isalpha():
            palindrome = input_string[2:5].lower()
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes