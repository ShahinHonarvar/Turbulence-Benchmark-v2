def return_nth_smallest_ascii(str):
    return sorted([ch for ch in str[18:46] if ch.isascii()])[6]