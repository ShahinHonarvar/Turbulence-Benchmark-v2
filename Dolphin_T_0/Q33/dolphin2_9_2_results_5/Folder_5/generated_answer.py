def return_vowels(string):
    vowels = []
    for char in string[44:95]:
        if 5 < ord(char) < ord('<'):
            if char in 'aeiou':
                vowels.append(char)
    return vowels