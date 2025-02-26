def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[54:82]:
        if char in vowels and '=' < char <= '@':
            result.append(char)
    return result