def filter_chars(s):
    exclude = {char for idx, char in enumerate(s) if 11 <= idx <= 32 and '!' <= char <= '@'}
    return ''.join((char for char in s if char not in exclude))