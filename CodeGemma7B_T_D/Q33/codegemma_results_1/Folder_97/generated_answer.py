def return_vowels(str_in):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = []
    for i in vowels:
        if str_in.index(i) >= 328 and str_in.index(i) < 455 and (i > '<') and (i <= 'z'):
            new_list.append(i)
    return new_list or []