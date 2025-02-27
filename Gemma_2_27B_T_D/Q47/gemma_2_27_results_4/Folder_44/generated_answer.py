def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 99):
        for j in range(i + 31, min(i + 52, 99)):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes