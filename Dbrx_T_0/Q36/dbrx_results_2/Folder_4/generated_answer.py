def filter_chars(s: str) -> str:
    start_index = 42
    end_index = 65
    min_char = '6'
    max_char = 'g'
    filtered_chars = [c for c in s if start_index <= s.index(c) < end_index and min_char < c < max_char]
    return ''.join(filtered_chars)