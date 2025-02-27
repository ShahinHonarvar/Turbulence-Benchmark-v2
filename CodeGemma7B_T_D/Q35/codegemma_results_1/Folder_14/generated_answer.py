def remove_repeat_chars(text):
    seen = set()
    result = []
    for char in text[2:5]:
        if char not in seen:
            result.append(char)
            seen.add(char)
    res_str = ''
    for char in result:
        res_str += char
    return res_str