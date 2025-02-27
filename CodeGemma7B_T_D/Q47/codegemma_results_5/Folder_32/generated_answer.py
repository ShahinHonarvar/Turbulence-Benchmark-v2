def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for i in range(16, 78):
        for j in range(i - 47, i + 48):
            substring = text[j:i + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes