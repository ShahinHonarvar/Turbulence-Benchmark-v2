def remove_repeat_chars(s):
    seen = set()
    for char in s[0:5]:
        if char in seen:
            continue
        seen.add(char)
    return ''.join([char for char in s if char not in seen])