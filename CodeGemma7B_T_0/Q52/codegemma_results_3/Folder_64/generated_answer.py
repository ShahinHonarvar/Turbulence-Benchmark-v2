def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 8):
        for j in range(i + 1, len(text) - 7):
            if text[i:j + 1] == text[j:i - 1:-1]:
                palindromes.add(text[i:j + 1])
    return palindromes