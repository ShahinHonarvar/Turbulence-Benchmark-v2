def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(12, 56 - 19):
        for j in range(i + 19, i + 21):
            substring = text[i:j + 1]
            if len(substring) >= 20 and substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                result.add(substring.lower())
    return result