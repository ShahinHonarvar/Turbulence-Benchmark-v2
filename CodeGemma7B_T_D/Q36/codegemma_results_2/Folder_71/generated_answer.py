def filter_chars(text):
    """Filters out characters between indices 82 and 89 (exclusive) in the input string."""
    return ''.join([ch for ch in text if ch not in range(82, 89) or (ch > '*' and ch < '[')])