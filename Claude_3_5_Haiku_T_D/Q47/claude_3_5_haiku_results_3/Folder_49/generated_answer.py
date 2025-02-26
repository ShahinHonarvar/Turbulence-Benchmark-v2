def palindromes_of_specific_lengths(text):
    if len(text) <= 100:
        return set()
    text = text[10:101].lower()
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(text) - length + 1):
            substring = text[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes