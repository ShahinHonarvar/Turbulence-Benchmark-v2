def return_n_smallest_chars(chars) -> list[str]:
    """Sorting characters in descending order by their ASCII values"""
    return sorted(chars, key=ord, reverse=True)[:61]