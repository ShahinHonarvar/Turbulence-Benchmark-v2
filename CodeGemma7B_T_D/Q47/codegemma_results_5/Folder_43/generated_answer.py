def palindromes_of_specific_lengths(text):
    start, end = (41, 89)
    result = set()
    text = text.lower()
    for i in range(start, end + 1):
        for j in range(i + 23, i + 38 + 1):
            if text[i:j] == text[i:j][::-1]:
                result.add(text[i:j])
    return result