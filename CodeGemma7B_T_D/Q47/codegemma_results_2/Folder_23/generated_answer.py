def palindromes_of_specific_lengths(text):
    start, end = (23, 94)
    min_len, max_len = (17, 55)
    palindromes = set()
    text = text.lower()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            substring = text[i:j + 1]
            if len(substring) < min_len or len(substring) > max_len:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes