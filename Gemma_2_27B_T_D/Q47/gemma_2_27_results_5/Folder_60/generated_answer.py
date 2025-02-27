def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 83):
        if i + 31 < len(text) and text[i:i + 32].replace(' ', '').isalpha() and (text[i:i + 32].lower() == text[i:i + 32].lower()[::-1]):
            palindromes.add(text[i:i + 32])
    for i in range(23, 83):
        if i + 33 < len(text) and text[i:i + 34].replace(' ', '').isalpha() and (text[i:i + 34].lower() == text[i:i + 34].lower()[::-1]):
            palindromes.add(text[i:i + 34])
    return palindromes