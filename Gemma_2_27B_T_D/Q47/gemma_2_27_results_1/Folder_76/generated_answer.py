def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i + 154, min(i + 183, 293)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes