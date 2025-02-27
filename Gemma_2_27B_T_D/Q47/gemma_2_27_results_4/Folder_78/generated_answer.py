def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 73):
        for j in range(i + 19, min(i + 56, 73) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes