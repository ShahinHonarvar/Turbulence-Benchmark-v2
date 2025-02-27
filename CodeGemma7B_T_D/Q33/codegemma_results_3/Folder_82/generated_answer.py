def return_vowels(string):
    vowels = ['e', 'i', 'o', 'u', 'a', 'E', 'I', 'O', 'U', 'A']
    return_value = []
    for i in range(86, 99):
        if string[i] in vowels and string[i] > 'E' and (string[i] <= 'r'):
            return_value.append(string[i])
    if not return_value:
        return_value = []
    return return_value