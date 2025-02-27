def palindromes_of_specific_lengths(text):
    result = set()
    text = text.lower()
    for i in range(15, 87):
        for length in range(51, 61):
            for j in range(i, i + length):
                if j + length - 1 >= len(text) or not text[j:j + length].isalpha():
                    break
                if text[j] == text[j + length - 1] and text[j:j + length] not in result:
                    result.add(text[j:j + length])
    return result