def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[10:84]
    result = set()
    for length in range(37, 61):
        for i in range(len(text) - length + 1):
            if text[i:i + length] == text[i:i + length][::-1]:
                result.add(text[i:i + length])
    return result