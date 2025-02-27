def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 101):
        for j in range(i + 9, min(i + 50, 100) + 1):
            substring = text[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes