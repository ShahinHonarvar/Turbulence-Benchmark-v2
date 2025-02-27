def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(100, 201):
        for j in range(i - 4, i + 1):
            if j >= 0 and j + 4 <= len(text) and (text[j:j + 5] == text[j:j + 5][::-1]):
                palindromes.add(text[j:j + 5])
            if j >= 0 and j + 6 <= len(text) and (text[j:j + 6] == text[j:j + 6][::-1]):
                palindromes.add(text[j:j + 6])
            if j >= 0 and j + 7 <= len(text) and (text[j:j + 7] == text[j:j + 7][::-1]):
                palindromes.add(text[j:j + 7])
            if j >= 0 and j + 8 <= len(text) and (text[j:j + 8] == text[j:j + 8][::-1]):
                palindromes.add(text[j:j + 8])
            if j >= 0 and j + 9 <= len(text) and (text[j:j + 9] == text[j:j + 9][::-1]):
                palindromes.add(text[j:j + 9])
    return palindromes