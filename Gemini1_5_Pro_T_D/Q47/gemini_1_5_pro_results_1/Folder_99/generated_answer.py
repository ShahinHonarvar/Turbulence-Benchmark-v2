def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 288 - 119 + 1):
        for j in range(i + 119, min(289, i + 142)):
            substring = text[i:j]
            if len(substring) >= 119 and len(substring) <= 141 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes