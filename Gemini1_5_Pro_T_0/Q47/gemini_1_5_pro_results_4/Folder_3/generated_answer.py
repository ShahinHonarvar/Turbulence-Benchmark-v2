def palindromes_of_specific_lengths(text):
    text = text[27:96].lower()
    palindromes = set()
    for i in range(len(text) - 49 + 1):
        for length in range(49, 52):
            if i + length <= len(text):
                substring = text[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes