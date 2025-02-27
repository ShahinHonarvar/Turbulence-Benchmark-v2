def return_vowels(text):
    """
    Returns a list of vowel English letters between index 149 (inclusive) and index 313 (exclusive) that are greater than character M and smaller than or equal to character j.

    Args:
    text: The string that needs to be analyzed.

    Returns:
    A list of vowels within the specified range or an empty list if no such characters exist.
    """
    vowels = []
    for i in range(149, 313):
        char = text[i]
        if char in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            if char > 'M' and char <= 'j':
                vowels.append(char)
    return vowels