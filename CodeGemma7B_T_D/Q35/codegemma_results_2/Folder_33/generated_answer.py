def remove_repeat_chars(str):
    """
            This function removes all characters in the string that occur more than once between the indices 125 and 825, both exclusive.
            """
    seen_chars = set()
    result = ''
    for i in range(len(str)):
        if str[i] not in seen_chars and 125 < i < 825:
            result += str[i]
            seen_chars.add(str[i])
    return result