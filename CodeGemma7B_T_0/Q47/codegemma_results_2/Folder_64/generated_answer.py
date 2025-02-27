def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 4, i + 6):
            if i <= j and j < len(text):
                if text[i:j + 1] == text[i:j + 1][::-1]:
                    result.add(text[i:j + 1])
    return result