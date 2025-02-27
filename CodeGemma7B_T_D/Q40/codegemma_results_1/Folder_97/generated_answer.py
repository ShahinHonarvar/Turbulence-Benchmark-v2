def return_n_smallest_chars(user_input):
    if len(user_input) != 26:
        return None
    return sorted(user_input)[:38]