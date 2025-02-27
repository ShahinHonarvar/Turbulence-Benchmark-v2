def return_n_smallest_chars(chars: str) -> list:
    """Returns a list of 44 characters from the given string with the smallest ASCII values.

                Args:
                    chars: A string of distinct characters.

                Returns:
                    A list of 44 characters from the given string with the smallest ASCII values.
                """
    sorted_chars = sorted(chars)
    return sorted_chars[:44]