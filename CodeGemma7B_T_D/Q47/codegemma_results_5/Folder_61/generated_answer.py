def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(0, 31):
        for j in range(20, 31):
            substring = text[i:i + j]
            if substring == substring[::-1]:
                substring = ''.join(filter(str.isalpha, substring))
                if len(substring) == j:
                    palindromes.add(substring.lower())
    return palindromes