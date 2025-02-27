def return_nth_smallest_ascii(s):
    if len(s) > 87:
        s = s[:88]
    return sorted(s)[13]