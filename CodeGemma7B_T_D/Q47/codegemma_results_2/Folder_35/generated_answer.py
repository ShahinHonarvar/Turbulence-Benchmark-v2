def palindromes_of_specific_lengths(text):
    specific_string = text[34:91].lower()
    result = set()
    for length in range(14, 40):
        for i in range(len(specific_string) - length + 1):
            substring = specific_string[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result