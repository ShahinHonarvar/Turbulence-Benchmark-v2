def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[1:9] if not '8' < char < 'm']
    return ''.join(filtered_chars + list(s[9:])) if len(filtered_chars) > 0 else s[1:9] + s[9:]