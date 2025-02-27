def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i, min(i + 160, 296)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and len(substring) >= 136 and (len(substring) <= 160) and substring.isalpha():
                palindromes.add(substring)
    return palindromes