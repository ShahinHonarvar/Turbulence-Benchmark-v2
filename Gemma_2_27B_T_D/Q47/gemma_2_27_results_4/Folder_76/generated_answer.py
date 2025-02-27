def palindromes_of_specific_lengths(text):
    subset = text[101:293]
    palindromes = set()
    for i in range(len(subset) - 153):
        for j in range(i + 154, min(i + 183, len(subset)) + 1):
            substring = subset[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes