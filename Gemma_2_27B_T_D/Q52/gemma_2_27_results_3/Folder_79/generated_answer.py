def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 63):
        substring = text[i:i + 64].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result