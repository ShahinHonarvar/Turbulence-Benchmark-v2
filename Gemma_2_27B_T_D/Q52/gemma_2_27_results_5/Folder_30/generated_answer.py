def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 93):
        substring = text[i:i + 94].lower()
        if substring == substring[::-1]:
            result.add(text[i:i + 94])
    return result