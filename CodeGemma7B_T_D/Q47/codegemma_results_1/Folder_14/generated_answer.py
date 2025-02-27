def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(10, 75):
        for j in range(i - 5, i + 3):
            if j <= 0 or j >= len(text) or text[i] != text[j]:
                continue
            name = text[j:i + 1]
            if 5 <= len(name) <= 8 and name == name[::-1]:
                palindromes.add(name)
    return palindromes