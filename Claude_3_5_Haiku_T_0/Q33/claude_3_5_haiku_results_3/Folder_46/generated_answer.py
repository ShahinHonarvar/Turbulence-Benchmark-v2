def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, 83):
        if i < len(string) and string[i] in vowels and ('%' < string[i] <= 'e'):
            result.append(string[i])
    return result