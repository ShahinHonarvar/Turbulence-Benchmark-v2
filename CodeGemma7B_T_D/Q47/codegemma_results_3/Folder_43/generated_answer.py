def palindromes_of_specific_lengths(txt):
    result = set()
    for i in range(41, 89 + 1):
        for j in range(i - 22, i + 1):
            if j >= 41 and j <= 89 and txt[j:i + 1].lower().isalpha():
                if txt[j:i + 1].lower() == txt[j:i + 1].lower()[::-1]:
                    result.add(txt[j:i + 1])
    return result