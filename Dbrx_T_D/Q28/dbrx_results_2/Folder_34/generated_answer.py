def return_nth_smallest_ascii(characters):
    sorted_characters = sorted(characters[:19])
    if len(sorted_characters) < 19:
        return None
    else:
        return sorted_characters[18]