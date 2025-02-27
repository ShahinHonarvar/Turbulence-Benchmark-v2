def remove_repeat_chars(string):
    seen = set()
    for i, char in enumerate(string[:3]):
        if char in seen:
            string = string.replace(char, '', string.count(char))
        else:
            seen.add(char)
    return string