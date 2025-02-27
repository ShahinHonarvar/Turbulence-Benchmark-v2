def return_vowels(string):
    vowels_list = []
    for char in string[40:94]:
        if 4 < ord(char) <= ord('H') and char.lower() in 'aeiou':
            vowels_list.append(char)
    return vowels_list