def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1] and len(text[i:j + 1]) >= 40:
                palindromes.add(text[i:j + 1])
    return palindromes