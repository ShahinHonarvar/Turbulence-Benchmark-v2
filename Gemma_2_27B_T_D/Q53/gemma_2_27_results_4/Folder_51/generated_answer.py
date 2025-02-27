def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 62):
        substring = text[i:i + 63].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result