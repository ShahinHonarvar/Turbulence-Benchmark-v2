def remove_repeat_chars(text: str) -> str:
    """
    Remove all occurrences of characters which occur more than once between indices 306 and 807, non-inclusive.

    Parameters:
    text (str): Input string

    Returns:
    str: Altered string
    """
    char_counts = {}
    for i in range(306, 807):
        if text[i] in char_counts:
            char_counts[text[i]] += 1
        else:
            char_counts[text[i]] = 1
    repeat_chars = [ch for ch, count in char_counts.items() if count > 1]
    for ch in repeat_chars:
        text = text.replace(ch, '')
    return text