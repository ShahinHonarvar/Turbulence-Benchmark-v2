def remove_repeat_chars(str):
    return ''.join([c for i, c in enumerate(str) if i not in range(10, 100) or i + 1 == str.find(c)])