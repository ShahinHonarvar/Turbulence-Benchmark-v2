def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 292 - 153):
        for j in range(i + 154, min(i + 183, 293)):
            substring = text[i:j]
            if len(substring) >= 154 and len(substring) <= 182 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes