def return_nth_smallest_ascii(s):
    target_characters = s[:19]
    sorted_characters = sorted(target_characters)
    return sorted_characters[18] if len(sorted_characters) >= 19 else None