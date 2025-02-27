def palindromes_of_specific_lengths(text):
    text = text[10:76]
    text = ''.join(filter(str.isalpha, text)).lower()
    result = set()
    for length in range(10, 21):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result