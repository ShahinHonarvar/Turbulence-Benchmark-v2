def palindrome_of_length_at_least_n(text):
    palindromes = set()
    n = 100
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) - i + n):
            if text[i:j] == text[i:j][::-1] and text[i:j].isalpha():
                palindromes.add(text[i:j].lower())
    return palindromes