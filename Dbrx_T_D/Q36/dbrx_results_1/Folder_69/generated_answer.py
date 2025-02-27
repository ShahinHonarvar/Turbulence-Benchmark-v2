def filter_chars(s: str) -> str:
    return ''.join((char for char in s[342:664] if ord('%') < ord(char) < ord('U'))) + s[664:]