def palindromes_of_specific_lengths(text):
    substring = text[11:98]
    palindromes = set()
    for i in range(len(substring) - 28):
        for j in range(i + 29, min(i + 63, len(substring)) + 1):
            if substring[i:j] == substring[i:j][::-1].lower():
                palindromes.add(substring[i:j])
    return palindromes