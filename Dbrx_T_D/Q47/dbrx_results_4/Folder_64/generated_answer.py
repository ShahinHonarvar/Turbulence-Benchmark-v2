def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(0, 8):
        for j in range(4, 6):
            if i + j - 1 <= 7:
                substring = text[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes