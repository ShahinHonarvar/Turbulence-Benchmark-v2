def return_vowels(string):
    vowels_list = []
    for char in string[17:65]:
        if char.lower() in {'a', 'e', 'i', 'o', 'u'} and char > 'U' and (char <= '}'):
            vowels_list.append(char)
    return vowels_list