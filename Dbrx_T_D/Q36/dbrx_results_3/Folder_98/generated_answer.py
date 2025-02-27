def filter_chars(s: str) -> str:
    start_index = 4
    end_index = 8
    chars_to_remove = {chr(i) for i in range(ord('1') + 1, ord('J'))}
    result = ''.join((char for char in s[start_index:end_index] if char not in chars_to_remove))
    return s[:start_index] + result + s[end_index:]