def return_vowels(my_str):
    list_of_vowels = []
    for i in range(36, 56):
        if my_str[i] in ['a', 'e', 'i', 'o', 'u'] and my_str[i] > '+' and (my_str[i] <= '/'):
            list_of_vowels.append(my_str[i])
    return list_of_vowels