def palindromes_of_specific_lengths(text):
    text = text.lower()
    start = 26
    end = 90
    result = set()
    for i in range(start, end + 1):
        for j in range(i + 26, end + 1):
            if text[i:j] == text[i:j][::-1]:
                result.add(text[i:j])
    return result