def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 84):
        substring = text[i:i + 85]
        if len(substring) == 85 and substring.lower() == substring.lower()[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes