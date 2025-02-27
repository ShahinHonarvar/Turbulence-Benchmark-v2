def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_list = []
    for letter in string:
        if letter in vowels and ord(letter) > ord('?') and (ord(letter) <= ord('k')):
            vowels_list.append(letter)
    return vowels_list