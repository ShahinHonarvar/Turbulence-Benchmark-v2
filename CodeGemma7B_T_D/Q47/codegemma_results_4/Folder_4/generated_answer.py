def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for start in range(12, 93):
        for end in range(start + 17, end + 67):
            substring = text[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes