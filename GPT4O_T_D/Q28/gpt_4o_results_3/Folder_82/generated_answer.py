def return_nth_smallest_ascii(input_string):
    return sorted(input_string[:15])[14] if len(input_string) >= 15 else None