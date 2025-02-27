def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(75, 96):
        for j in range(i + 7, min(i + 10, 96)):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes