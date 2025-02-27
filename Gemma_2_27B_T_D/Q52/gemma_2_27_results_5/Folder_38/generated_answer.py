def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 37):
        substring = text[i:i + 38]
        if substring.lower() == substring.lower()[::-1]:
            result.add(substring)
    return result