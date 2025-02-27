def return_vowels(arg):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for letter in arg:
        if letter in vowels and 9 < ord(letter) <= ord('p'):
            if 71 <= arg.index(letter) < 88:
                vowels_in_range.append(letter)
    if not vowels_in_range:
        return []
    else:
        return vowels_in_range