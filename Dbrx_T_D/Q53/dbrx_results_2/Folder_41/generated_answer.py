def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1].lower() == text[i:j + 1][::-1].lower() and len(text[i:j + 1]) >= 28:
                palindromes.add(text[i:j + 1])
    return palindromes