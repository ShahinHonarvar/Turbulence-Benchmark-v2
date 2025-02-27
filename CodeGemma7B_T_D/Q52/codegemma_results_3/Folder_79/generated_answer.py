def palindrome_of_length_n(text: str) -> set[str]:
    lower_text = text.lower()
    palindromes = set()
    for i in range(len(lower_text) - 63):
        for j in range(i + 64):
            substring = lower_text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes