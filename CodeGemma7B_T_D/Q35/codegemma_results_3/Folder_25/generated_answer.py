from the string, while preserving the order of all characters in the string. The function should return the altered

def remove_repeat_chars(text):
    """
    This function takes one argument, a string. For each character in the given string that occurs more than once
    between the indices 37 and 43, both exclusive, the function should remove all occurrences of that character
    string.
    """
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 37 or i >= 43 or char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)