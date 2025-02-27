def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 85):
        for j in range(i + 21, i + 32):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes