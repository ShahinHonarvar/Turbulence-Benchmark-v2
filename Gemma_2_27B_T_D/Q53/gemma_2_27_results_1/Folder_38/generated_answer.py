def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 55):
        substring = text[i:i + 56]
        if substring.lower() == substring[::-1].lower():
            result.add(substring)
    return result