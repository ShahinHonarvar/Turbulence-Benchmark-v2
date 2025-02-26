def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[40:94]:
        if char in vowels and '4' < char <= 'H':
            result.append(char)
    return result