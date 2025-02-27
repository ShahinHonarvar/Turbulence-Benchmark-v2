def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 85 + 1):
        for j in range(i + 26, i + 31 + 1):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    if not palindromes:
        return set()
    return palindromes