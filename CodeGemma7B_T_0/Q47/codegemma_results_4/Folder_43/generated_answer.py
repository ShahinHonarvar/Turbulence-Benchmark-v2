def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(41, 90):
        for j in range(i - 22, i + 1):
            if j >= 0 and j + 22 <= len(text):
                substring = text[j:j + 23]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    for i in range(41, 90):
        for j in range(i - 37, i + 1):
            if j >= 0 and j + 37 <= len(text):
                substring = text[j:j + 38]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes