def return_nth_smallest_ascii(s):
    relevant_characters = s[10:74]
    sorted_characters = sorted(relevant_characters, key=ord)
    return sorted_characters[8] if len(sorted_characters) >= 9 else None