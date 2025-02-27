def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 92):
        for j in range(i + 93, len(text) + 1):
            substring = text[i:j]
            if ''.join(filter(str.isalpha, substring)).lower() == ''.join(filter(str.isalpha, substring)).lower()[::-1]:
                palindromes.add(substring)
    return palindromes