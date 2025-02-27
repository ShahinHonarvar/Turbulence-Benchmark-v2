def filter_chars(str):
    """
    Filter characters between index 71 and 94, which are not within K and a.
    """
    return ''.join([c for c in str if not (71 <= ord(c) <= 94 and ord(c) < ord('K') or ord('a') <= ord(c))])