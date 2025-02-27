def insert_after_character(s: str) -> str:
    """Inserts character '0' immediately succeeding any occurrences of character 'a' in the input string."""
    return ''.join([char + '0' if char == 'a' else char for char in s])