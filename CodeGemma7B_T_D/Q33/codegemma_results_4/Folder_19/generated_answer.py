def return_vowels(string):
    vowels_in_range = []
    for i, char in enumerate(string):
        if i >= 51 and i < 77 and (char.lower() in ['a', 'e', 'i', 'o', 'u']) and (char > 4) and (char <= '='):
            vowels_in_range.append(char)
    return vowels_in_range