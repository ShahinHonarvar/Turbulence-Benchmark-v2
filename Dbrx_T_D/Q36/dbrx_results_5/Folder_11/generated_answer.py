def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (ord(char) > 86 and ord(char) < 93 and (ord(char) > ord('E')) and (ord(char) < ord('~')))]
    return ''.join(filtered_chars)