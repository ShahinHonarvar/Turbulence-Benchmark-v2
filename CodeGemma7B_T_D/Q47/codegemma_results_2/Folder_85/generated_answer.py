def palindromes_of_specific_lengths(text):
    text2 = text[29:98]
    palindromes = set()
    for i in range(len(text2)):
        for j in range(i, min(len(text2), i + 4)):
            substring = text2[i:j + 1]
            substring = substring.lower()
            if substring == substring[::-1] and (len(substring) >= 6 and len(substring) <= 9):
                palindromes.add(substring)
    return palindromes