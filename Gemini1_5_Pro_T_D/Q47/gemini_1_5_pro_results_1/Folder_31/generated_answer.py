def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 36, min(84, i + 60)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes