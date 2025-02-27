def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(17, 72 + 1):
        for j in range(i, 72 + 1):
            if 50 <= j - i + 1 <= 51:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    result.add(substring)
    return result