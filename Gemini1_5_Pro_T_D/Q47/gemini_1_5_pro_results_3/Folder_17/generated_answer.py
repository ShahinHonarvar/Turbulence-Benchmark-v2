def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 96):
        for length in range(52, 56):
            if i + length <= 96:
                substring = text[i:i + length]
                if substring.isalpha() and len(substring) == length and (substring.lower() == substring[::-1].lower()):
                    palindromes.add(substring)
    return palindromes