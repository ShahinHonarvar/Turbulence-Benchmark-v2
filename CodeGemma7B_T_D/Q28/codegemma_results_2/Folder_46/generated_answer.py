def return_nth_smallest_ascii(user_string):
    return sorted([c for c in user_string[34:86] if c.isascii()])[19]