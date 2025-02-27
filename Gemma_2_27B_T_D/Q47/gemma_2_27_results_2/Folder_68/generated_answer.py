def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 50, min(i + 100, len(text)) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes