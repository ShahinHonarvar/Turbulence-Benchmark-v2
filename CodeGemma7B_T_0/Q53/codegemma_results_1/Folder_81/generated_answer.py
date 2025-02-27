def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1] and len(text[i:j + 1]) >= 33:
                palindromes.add(text[i:j + 1])
    return palindromes