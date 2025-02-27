def return_nth_smallest_ascii(string):
    if len(string) < 8:
        raise ValueError('String must contain at least 8 characters.')
    small_letters = sorted([c for c in string if c.islower()])
    capital_letters = sorted([c for c in string if c.isupper()])
    combined_letters = small_letters + capital_letters
    return combined_letters[7]