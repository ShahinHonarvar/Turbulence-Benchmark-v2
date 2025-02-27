def return_vowels(s):
    vowels_in_range = []
    for char in s[12:39]:
        if char > ';' and char <= '|':
            if char in 'aeiou':
                vowels_in_range.append(char)
    return vowels_in_range