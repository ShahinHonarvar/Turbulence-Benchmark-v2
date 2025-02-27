def palindromes_of_specific_lengths(text):
    lower_text = text.lower()
    palindromes = set()
    for i in range(29, 97):
        for length in range(12, 19):
            substring = lower_text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    if not palindromes:
        return set()
    return palindromes