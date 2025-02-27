def return_vowels(string):
    vowels = 'aeiou'
    return_list = []
    for i in range(56, 90):
        if string[i] > 'K' and string[i] <= 'z':
            if string[i] in vowels:
                return_list.append(string[i])
    return return_list