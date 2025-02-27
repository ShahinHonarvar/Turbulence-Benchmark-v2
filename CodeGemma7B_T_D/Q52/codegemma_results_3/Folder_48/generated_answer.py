def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    n = 186
    used = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring not in used and len(substring) == n and (substring == substring[::-1]):
                result.add(substring)
                used.add(substring)
    return result