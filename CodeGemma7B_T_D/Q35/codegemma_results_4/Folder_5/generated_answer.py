def remove_repeat_chars(string):
    results = ''
    for i in range(2, 8):
        results += string[i]
    seen = ''
    for char in results:
        if char not in seen:
            seen += char
    return seen