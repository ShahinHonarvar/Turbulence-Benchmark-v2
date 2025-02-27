def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(15, 96):
        for j in range(20, 67):
            if i + j <= 96:
                substring = text[i:i + j]
                if len(substring) >= 20 and len(substring) <= 66 and (substring.lower() == substring.lower()[::-1]) and all((letter.isalpha() for letter in substring)):
                    result.add(substring)
    return result