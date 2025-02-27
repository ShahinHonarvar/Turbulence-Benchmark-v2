def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 18):
        for j in range(i + 1, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes