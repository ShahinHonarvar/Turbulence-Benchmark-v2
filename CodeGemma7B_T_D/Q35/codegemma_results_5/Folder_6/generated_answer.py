def remove_repeat_chars(s):
    """
            This function remove the repeated chars in a string between the indices 20 and 93.
            """
    seen = set()
    seen_indices = []
    new_str = ''
    for i, c in enumerate(s):
        if 20 < i <= 93 and c in seen:
            seen_indices.append(i)
        else:
            new_str += c
            seen.add(c)
    return new_str