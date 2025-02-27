def remove_repeat_chars(s):
    """
    Write a function called 'remove_repeat_chars' that takes one argument, a string.
    For each character in the given string that occurs more than once between the indices 0 and 3, both exclusive, the function should remove all occurrences of that character from the string, while preserving the order of all characters in the string.
    The function should return the altered string.
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen and 0 < s.index(char) < 3:
            seen.add(char)
            result.append(char)
    return ''.join(result)