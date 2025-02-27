import functools

def return_n_greatest_chars(chars: str) -> list[str]:
    """
    Sorts a string of distinct characters in descending order of their ASCII values and returns a list of 68 characters with the greatest values.
    """
    if len(chars) != len(set(chars)):
        raise ValueError('Input string must contain only distinct characters.')
    if len(chars) > 68:
        raise ValueError('Input string cannot contain more than 68 characters.')
    chars = sorted(chars, key=functools.cmp_to_key(ord), reverse=True)
    return chars[:68]