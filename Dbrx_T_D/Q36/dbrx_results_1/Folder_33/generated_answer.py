def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[298:418] if not '9' < char < 'P']
    return s[:298] + ''.join(filtered_chars) + s[418:]