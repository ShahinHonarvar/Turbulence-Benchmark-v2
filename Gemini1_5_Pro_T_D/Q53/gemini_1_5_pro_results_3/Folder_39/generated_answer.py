def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 68):
        for j in range(i + 69, len(text) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes