def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if not 88 <= i <= 90 or (char < 'J' or char > 'Q')]
    return ''.join(filtered_chars)