def filter_chars(s: str) -> str:
    return ''.join((char for char in s if char < 't' or char > 'x' or ord(char) not in range(ord(s[42]), ord(s[68]))))