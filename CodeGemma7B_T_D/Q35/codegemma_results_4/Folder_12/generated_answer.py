def remove_repeat_chars(text):
    """
            Write a function called 'remove_repeat_chars' that takes one argument,
            a string. For each character in the given string that occurs more than once
            between the indices 16 and 87, both exclusive, the function should
            remove all occurrences of that character from the string, while
            preserving the order of all characters in the string. The function
            should return the altered string.
            """
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if i < 16 or i >= 87:
            result.append(char)
            continue
        if char in seen_chars:
            continue
        seen_chars.add(char)
        result.append(char)
    return ''.join(result)