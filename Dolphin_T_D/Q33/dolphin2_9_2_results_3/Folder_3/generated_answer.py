def return_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    return_list = [char for char in string[50:77] if char > '#' and char <= 'r' and (char in vowel_list)]
    return return_list