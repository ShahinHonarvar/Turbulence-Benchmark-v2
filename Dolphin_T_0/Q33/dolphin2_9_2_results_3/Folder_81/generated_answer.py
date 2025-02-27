def return_vowels(my_string):
    vowels = []
    for i in range(20, 43):
        if 5 < ord(my_string[i]) <= ord('M') and my_string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(my_string[i])
    return vowels