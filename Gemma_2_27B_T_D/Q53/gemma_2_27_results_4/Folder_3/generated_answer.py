def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 58):
        substring = text[i:i + 59]
        if substring.lower() == substring[::-1].lower():
            result.add(substring)
    return result