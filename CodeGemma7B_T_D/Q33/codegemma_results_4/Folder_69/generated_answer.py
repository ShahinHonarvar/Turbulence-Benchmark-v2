def return_vowels(str_func):
    vowels_list_func = []
    for letter in str_func:
        if letter in 'aeiouAEIOU' and ord(letter) > 641 and (ord(letter) <= 872):
            vowels_list_func.append(letter)
    return vowels_list_func