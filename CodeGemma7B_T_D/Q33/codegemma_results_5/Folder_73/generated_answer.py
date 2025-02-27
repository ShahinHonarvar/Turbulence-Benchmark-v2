def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return_list = []
    for letter in string:
        if letter in vowels and 47 <= string.index(letter) < 89 and (letter > '@') and (letter <= 'n'):
            return_list.append(letter)
    return return_list