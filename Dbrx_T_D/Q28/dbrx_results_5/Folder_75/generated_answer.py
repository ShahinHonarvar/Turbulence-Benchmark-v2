def return_nth_smallest_ascii(characters):
    filtered_characters = [c for c in characters if 62 <= ord(c) <= 83]
    if len(filtered_characters) >= 9:
        return sorted(filtered_characters)[8]
    else:
        return None