def palindromes_of_specific_lengths(text):
    text = text[2:9].lower()
    result = set()
    for i in range(len(text) - 2):
        for j in range(i + 3, min(len(text) + 1, i + 5)):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result