def remove_repeat_chars(str):
    """
            This function takes one argument, a string.
            For each character in the given string that occurs more than once between the indices 72 and 93, both exclusive, the function should remove all occurrences of that character from the string, while preserving the order of all characters in the string.
            The function should return the altered string.
            """
    result = list(str[:72])
    seen = set()
    for i in range(72, 93):
        char = str[i]
        if char not in seen:
            seen.add(char)
            result.append(char)
    result.extend(list(str[93:]))
    return ''.join(result)