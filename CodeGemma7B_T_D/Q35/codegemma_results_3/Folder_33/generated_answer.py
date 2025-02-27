def remove_repeat_chars(str_arg):
    """
            Function to remove repeated characters between indices 125 and 825,
            inclusive.

            Args:
                str_arg: Input string.

            Returns:
                Altered string with repeated characters removed.
            """
    seen = set()
    updated_string = ''
    for i, char in enumerate(str_arg):
        if i == 0 or i == len(str_arg) - 1:
            updated_string += char
        elif 125 < i < 825:
            if char not in seen:
                updated_string += char
                seen.add(char)
    return updated_string