def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 68):
        substring = text[i:i + 69].lower()
        if substring == substring[::-1]:
            result.add(text[i:i + 69])
    return result