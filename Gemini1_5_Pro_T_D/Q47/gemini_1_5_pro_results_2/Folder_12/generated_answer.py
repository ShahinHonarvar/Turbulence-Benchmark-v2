def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 88 - 17):
        for length in range(18, 22):
            substring = text[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1] and (len(substring) == length):
                palindromes.add(text[i:i + length])
    return palindromes