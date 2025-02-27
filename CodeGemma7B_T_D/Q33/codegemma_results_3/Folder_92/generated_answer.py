def return_vowels(my_string):
    vowels = []
    for char in my_string[3:8]:
        if char in 'aeiouAEIOU' and char > ';' and (char <= 'D'):
            vowels.append(char)
    return vowels