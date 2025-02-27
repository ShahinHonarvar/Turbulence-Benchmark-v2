def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(75, 96):
        for j in range(i + 7, min(i + 10, 96)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result