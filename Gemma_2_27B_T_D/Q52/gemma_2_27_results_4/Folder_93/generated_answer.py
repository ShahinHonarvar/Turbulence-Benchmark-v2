def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 44):
        substring = text[i:i + 45].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result