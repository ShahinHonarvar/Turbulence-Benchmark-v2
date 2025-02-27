def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 39):
        for j in range(i + 1, len(text) - 39 + i + 1):
            if text[i:j] == text[j:i:-1]:
                palindromes.add(text[i:j + 1])
    return palindromes