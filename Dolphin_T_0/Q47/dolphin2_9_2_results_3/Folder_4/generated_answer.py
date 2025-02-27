def palindromes_of_specific_lengths(text):
    palindromes = set()
    for length in range(17, 67):
        for i in range(12, 93):
            if i + length <= 93:
                substring = text[i:i + length]
                if all((c.isalpha() for c in substring.lower())) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes