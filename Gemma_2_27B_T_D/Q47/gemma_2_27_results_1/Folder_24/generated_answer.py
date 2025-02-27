def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 42, min(i + 78, 93)):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes