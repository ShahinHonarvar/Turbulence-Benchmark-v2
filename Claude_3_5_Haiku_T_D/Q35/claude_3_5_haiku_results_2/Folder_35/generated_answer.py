def remove_repeat_chars(string):
    substring = string[78:84]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in string if char not in repeated_chars or string.index(char) <= 77 or string.index(char) >= 84))
    return result