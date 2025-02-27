def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 88):
        for j in range(i + 89, len(text) + 1):
            substring = text[i:j]
            if ''.join(filter(str.isalpha, substring)).lower() == ''.join(filter(str.isalpha, substring))[::-1].lower() and len(substring) >= 89:
                palindromes.add(substring)
    return palindromes