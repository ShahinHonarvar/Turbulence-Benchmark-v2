def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 61):
        substring = text[i:i + 62].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result