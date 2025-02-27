def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 88):
        for j in range(52, 57):
            for k in range(i - j + 1):
                substring = text[i - k:i + 1 + k]
                if substring == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes