def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 300):
        for j in range(i + 2, min(i + 11, 300)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes