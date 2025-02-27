def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(i, min(i + 134, 284)):
            substring = text[i:j + 1]
            if len(substring) >= 115 and len(substring) <= 134 and (substring.lower() == substring[::-1].lower()) and substring.isalpha():
                palindromes.add(substring)
    return palindromes