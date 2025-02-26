def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 171 < i < 636 and 'c' < s[i] < 's':
            char_to_remove = s[i]
            result = [char for char in s if char != char_to_remove]
            s = ''.join(result)
    return s