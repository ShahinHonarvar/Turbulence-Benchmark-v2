def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 140, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes