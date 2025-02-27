def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_string = string[56:96]
    result_list = [char for char in sub_string if char > '&' and char <= 'T' and (char in vowels)]
    return result_list