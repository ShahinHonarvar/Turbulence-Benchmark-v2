def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(10, 97):
        for j in range(i - 44, i + 5):
            if j >= 0 and j <= 96:
                substring = text[j:i + 1]
                if substring == substring[::-1]:
                    result.add(substring)
    return result