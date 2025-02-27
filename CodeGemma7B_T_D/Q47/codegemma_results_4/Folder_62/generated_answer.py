def palindromes_of_specific_lengths(text):
    if len(text) < 64:
        return set()
    palindromes = set()
    for i in range(26, 88):
        for j in range(i, 88):
            substring = text[i:j + 1]
            if substring == substring[::-1] and 52 <= len(substring) <= 56:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes