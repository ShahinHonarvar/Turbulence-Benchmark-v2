def return_vowels(string):
    vowels = []
    for i in range(10, 82):
        if i < len(string) and string[i] in 'aeiouAEIOU' and ('$' < string[i] <= '@'):
            vowels.append(string[i])
    return vowels