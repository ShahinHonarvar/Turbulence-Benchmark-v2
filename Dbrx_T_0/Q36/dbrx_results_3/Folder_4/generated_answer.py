def filter_chars(s: str) -> str:
    start_index = 42
    end_index = 65
    min_char = '6'
    max_char = 'g'
    filtered_chars = [char for char in s[start_index:end_index] if not min_char <= char <= max_char]
    return s[:start_index] + ''.join(filtered_chars) + s[end_index:]