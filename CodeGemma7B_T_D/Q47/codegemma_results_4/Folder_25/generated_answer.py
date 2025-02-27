def palindromes_of_specific_lengths(text):
    results = set()
    text = text.lower()
    for i in range(26, 85):
        for j in range(i - 29, i + 27):
            if j >= 0 and j <= len(text) - 1:
                substring = text[j:i]
                if substring == substring[::-1]:
                    if len(substring) >= 30 and len(substring) <= 46:
                        results.add(substring)
    return results