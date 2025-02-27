def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 82 - 31):
        for length in range(32, 35):
            substring = text[i:i + length + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes