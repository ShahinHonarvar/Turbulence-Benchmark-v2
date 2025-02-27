def palindromes_of_specific_lengths(text):
    output = set()
    text = text.lower()
    for i in range(1, 8):
        for j in range(i, 8):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) in [3, 4]:
                output.add(substring)
    return output