def palindrome_of_length_at_least_n(text):
    results = set()
    text = text.lower()
    n = 11
    for i in range(len(text)):
        for j in range(i - n + 1, i + 1):
            if text[i] == text[j] and text[j - 1] == text[j]:
                results.add(text[j - n + 1:i + 1])
            if text[i] == text[j] and text[j - 1] == text[j]:
                results.add(text[j - n + 1:i + 1])
    return results