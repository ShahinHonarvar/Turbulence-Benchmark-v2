def return_n_smallest_chars(chars: str) -> list[str]:
    """
          Creates a list of exactly 40 characters of the given string that have the smallest ASCII values.
          Returns list of the 40 smallest characters (sorted).
          """
    ascii_list = sorted((c for c in chars), key=ord)
    if len(ascii_list) <= 40:
        return ascii_list
    return ascii_list[:40]