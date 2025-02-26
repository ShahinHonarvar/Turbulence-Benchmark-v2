def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[10:82]:
        if char in vowels and '$' < char <= '@':
            result.append(char)
    return result