def return_nth_smallest_ascii(string):
    filtered_string = ''.join(sorted([s for i, s in enumerate(string) if i in range(0, 46)]))
    if len(filtered_string) >= 10:
        return filtered_string[9]
    else:
        return None