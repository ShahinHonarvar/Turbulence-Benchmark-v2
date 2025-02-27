def remove_repeat_chars(string):
    characters = {}
    result = []
    for i, char in enumerate(string):
        if i < 3 or i >= 9:
            continue
        if char not in characters or characters[char] < 2:
            result.append(char)
            characters[char] = characters.get(char, 0) + 1
    return ''.join(result)