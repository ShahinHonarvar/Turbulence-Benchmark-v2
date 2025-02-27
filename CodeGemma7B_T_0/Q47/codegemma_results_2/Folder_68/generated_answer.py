def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(50):
        for j in range(i + 50, min(i + 101, len(text))):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result