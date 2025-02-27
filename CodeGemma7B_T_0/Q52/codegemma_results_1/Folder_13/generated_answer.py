def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 205):
        for j in range(i + 1, len(text) - 204):
            if text[i:j + 1] == text[j:i - 1:-1]:
                palindromes.add(text[i:j + 1])
    return palindromes