def filter_chars(text):
    """
            Filters out characters between indices 58 and 81 (exclusive) in the input string,
            removing characters greater than '5' and smaller than '>'.

            Args:
                text: The input string.

            Returns:
                The altered string with filtered characters.
            """
    filtered_text = []
    for i, char in enumerate(text):
        if i >= 58 and i < 81:
            if char > '5' and char < '>':
                continue
        filtered_text.append(char)
    return ''.join(filtered_text)