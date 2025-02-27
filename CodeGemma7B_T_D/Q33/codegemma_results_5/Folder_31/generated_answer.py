def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(len(string)):
        if string[i] in vowels and string[i] > '%' and (string[i] <= 'G') and (i >= 65) and (i < 70):
            return_list.append(string[i])
    return return_list