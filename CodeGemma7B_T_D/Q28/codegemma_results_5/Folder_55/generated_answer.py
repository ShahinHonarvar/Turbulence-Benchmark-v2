def return_nth_smallest_ascii(s):
    if not isinstance(s, str):
        raise TypeError('Input must be a string.')
    if not all((len(c) == 1 for c in s)):
        raise ValueError('Input string must contain only distinct characters.')
    substring = s[0:13]
    ascii_values = [ord(c) for c in substring]
    return chr(min(ascii_values))