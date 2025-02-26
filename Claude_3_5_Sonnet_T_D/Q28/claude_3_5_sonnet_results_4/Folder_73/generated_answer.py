def return_nth_smallest_ascii(string):
    relevant_chars = string[:70]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None