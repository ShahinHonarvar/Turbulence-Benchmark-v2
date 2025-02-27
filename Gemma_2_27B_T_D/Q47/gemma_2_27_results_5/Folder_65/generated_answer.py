def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for length in range(20, 67):
            if i + length <= 96:
                substring = text[i:i + length]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes