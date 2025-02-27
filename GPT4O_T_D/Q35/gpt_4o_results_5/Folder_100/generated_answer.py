def remove_repeat_chars(s):
    count = {}
    for char in s[45:78]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    chars_to_remove = {char for char, c in count.items() if c > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 45 <= s.index(char) < 78))