def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(i + 114, min(284, i + 135)):
            substring = text[i:j]
            if len(substring) >= 115 and len(substring) <= 134 and substring.isalpha():
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes