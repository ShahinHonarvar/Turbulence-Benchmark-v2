def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    if not palindromes:
        return set()
    return palindromes