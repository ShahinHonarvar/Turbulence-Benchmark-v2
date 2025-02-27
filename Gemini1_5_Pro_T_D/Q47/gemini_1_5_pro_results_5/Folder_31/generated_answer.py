def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 36, min(84, i + 61)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes