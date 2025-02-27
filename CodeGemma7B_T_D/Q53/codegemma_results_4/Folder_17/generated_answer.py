def palindrome_of_length_at_least_n(text):
    text = text.lower()
    distinct_chars = set(text)
    result = set()
    if len(distinct_chars) < 36:
        return result
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result