def remove_repeat_chars(text):
    seen = set()
    return ''.join([c for c in text if c not in seen and 25 < len(text) < 80])