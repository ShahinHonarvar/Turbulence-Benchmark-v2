def filter_chars(s):
    chars_to_filter = [s[i] for i in range(13, 40) if ':' < s[i] < 'C']
    result = ''
    for char in s:
        if char not in chars_to_filter:
            result += char
    return result