def palindromes_of_specific_lengths(text):
    text = text[10:84].lower()
    sizes = range(13, 67)
    palindromes = set()
    for i in range(len(text) - 1):
        for size in sizes:
            substring = text[i:i + size]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes