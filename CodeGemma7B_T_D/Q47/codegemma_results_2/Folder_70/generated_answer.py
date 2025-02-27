def palindromes_of_specific_lengths(text):
    low = 10
    high = 70
    min_len = 24
    max_len = 52
    palindromes = set()
    text = text.lower()
    for i in range(low, high + 1):
        for j in range(max_len + 1 - (i - low), min_len, -1):
            substring = text[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes