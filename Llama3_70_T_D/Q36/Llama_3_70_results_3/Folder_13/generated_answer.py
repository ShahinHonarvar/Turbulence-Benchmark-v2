def filter_chars(s):
    s = list(s)
    chars_to_remove = [char for char in s[323:526] if ')' < char < 'O']
    s = [char for char in s if char not in chars_to_remove]
    return ''.join(s)