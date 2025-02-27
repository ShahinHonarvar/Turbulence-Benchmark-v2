def remove_repeat_chars(s):
    check_span = s[37:52]
    repeated_chars = {char for char in check_span if check_span.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))