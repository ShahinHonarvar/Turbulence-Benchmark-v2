def palindrome_of_length_n(text: str) -> set[str]:

    def is_palindrome(text: str):
        return text == text[::-1]
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and len(substring) == 99:
                palindromes.add(substring)
    return palindromes