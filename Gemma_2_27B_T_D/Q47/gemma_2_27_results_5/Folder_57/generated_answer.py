def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(16, 95):
        for j in range(i + 39, min(i + 53, 95)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result