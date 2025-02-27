def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(5, 8):
        char = input_string[i]
        if char.isalpha():
            palindrome = input_string[5:i + 1].lower()
            if is_palindrome(palindrome) and len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes