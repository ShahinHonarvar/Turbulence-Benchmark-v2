def return_vowels(string):
    vowels = 'aeiou'
    sub_string = string[64:82]
    return_list = []
    for character in sub_string:
        if character in vowels and character > 'a' and (character <= 'z'):
            return_list.append(character)
    return return_list