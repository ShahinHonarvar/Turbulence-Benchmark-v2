def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[23:45] if '3' < char < 'I']
    return s[:23] + ''.join(filtered_chars) + s[45:]