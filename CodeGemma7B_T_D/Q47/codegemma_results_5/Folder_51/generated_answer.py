def palindromes_of_specific_lengths(text):
    palindromes = set()
    lowered_text = text.lower()
    indices = range(2, 9)
    for start in indices:
        for end in range(start + 3, start + 5):
            substring = lowered_text[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes