def palindrome_of_length_at_least_n(text):
    text = ''.join(filter(str.isalpha, text.lower()))
    palindromes = set()
    n = 56
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes