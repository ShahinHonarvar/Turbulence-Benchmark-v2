def palindrome_of_length_n(text: str) -> set[str]:
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 17):
        palindrome = text[i:i + 18]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes