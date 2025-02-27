def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 51, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes