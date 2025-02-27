def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(30, 96):
        for j in range(i + 34, i + 56):
            if text[i:j] == text[j - 1:i - 1:-1]:
                result.add(text[i:j])
    return result