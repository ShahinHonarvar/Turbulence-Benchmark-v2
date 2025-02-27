def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 88 - 17):
        for length in range(18, 22):
            if i + length <= 89:
                substring = text[i:i + length]
                if substring.isalpha() and len(substring) >= 18 and (len(substring) <= 21) and (substring.lower() == substring[::-1].lower()):
                    palindromes.add(substring)
    return palindromes