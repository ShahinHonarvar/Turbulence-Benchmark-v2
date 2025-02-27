def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 2, len(text) + 1):
            if text[i:j] == text[j - 2:i:-1] and len(text[i:j]) >= 88:
                palindromes.add(text[i:j])
    return palindromes