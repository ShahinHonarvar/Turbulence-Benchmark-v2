def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 91):
        substring = text[i:i + 92].lower()
        if substring == substring[::-1]:
            palindromes.add(text[i:i + 92])
        for j in range(i + 93, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes