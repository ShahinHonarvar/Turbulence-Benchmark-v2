def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 82):
        for j in range(i + 83, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes