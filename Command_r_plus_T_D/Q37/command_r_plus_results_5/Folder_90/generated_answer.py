def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (348 <= s.index(char) <= 852 and 'J' <= char <= 'b')]
    return ''.join(filtered_chars)