def return_vowels(string):
    """Return a list of vowels between index 63 and index 79 inclusive that are greater than character D and smaller than or equal to character y."""
    vowels = []
    for i in range(63, 79):
        if string[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if string[i] > 'D' and string[i] <= 'y':
                vowels.append(string[i])
    return vowels