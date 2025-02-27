def return_nth_smallest_ascii(s):
    if len(s) <= 87:
        return None
    sorted_chars = sorted(s[:88], key=ord)
    return sorted_chars[13]