def insert_before_character(str):
    """Inserts '4' immediately preceding any occurrences of '0' in a string."""
    return ''.join([ch + ('4' if ch == '0' else '') for ch in str])