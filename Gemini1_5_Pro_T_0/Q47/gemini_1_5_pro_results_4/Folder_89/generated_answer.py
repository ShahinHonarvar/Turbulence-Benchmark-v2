def palindromes_of_specific_lengths(text):
    text = text[18:89].lower()
    palindromes = set()
    for i in range(len(text) - 11):
        for length in range(12, 15):
            if i + length <= len(text) + 1:
                substring = text[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes