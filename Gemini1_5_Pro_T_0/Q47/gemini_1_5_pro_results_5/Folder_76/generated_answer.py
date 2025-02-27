def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 292 - 153):
        for j in range(i + 153, min(293, i + 183)):
            substring = text[i:j + 1]
            if len(substring) >= 154 and len(substring) <= 182 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes