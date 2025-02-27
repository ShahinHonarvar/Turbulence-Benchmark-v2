def remove_repeat_chars(string):
    char_freq = {}
    for char in string[462:995]:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    chars_to_remove = set()
    for char, freq in char_freq.items():
        if freq > 1:
            chars_to_remove.add(char)
    altered_string = ''
    for char in string:
        if char not in chars_to_remove:
            altered_string += char
    return altered_string