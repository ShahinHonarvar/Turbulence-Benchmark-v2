def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 96):
        for j in range(52, 56):
            if i + j <= 96:
                substring = text[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes