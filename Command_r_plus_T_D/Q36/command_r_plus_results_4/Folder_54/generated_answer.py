def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[18:38] if ')' < char < 'P']
    return s.translate(str.maketrans('', '', ''.join(chars_to_remove)))