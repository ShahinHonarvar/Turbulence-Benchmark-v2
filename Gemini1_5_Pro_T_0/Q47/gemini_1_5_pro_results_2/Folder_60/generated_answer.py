def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(23, 82 - 31):
        for j in range(i + 32, min(i + 35, 83)):
            substring = text[i:j]
            if len(substring) >= 32 and len(substring) <= 34 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                result.add(substring)
    return result