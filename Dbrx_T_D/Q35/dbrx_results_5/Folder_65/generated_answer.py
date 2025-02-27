def remove_repeat_chars(string):
    substring = string[50:76]
    duplicates = []
    for char in set(substring):
        if substring.count(char) > 1:
            duplicates.append(char)
    for char in duplicates:
        string = string.replace(char, '', substring.count(char))
    return string