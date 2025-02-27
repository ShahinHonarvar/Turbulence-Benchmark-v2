def remove_repeat_chars(s):
    chars_count = {}
    for char in s[477:709]:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    to_remove = {char for char, count in chars_count.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or not 476 < s.index(char) < 709))
    return result