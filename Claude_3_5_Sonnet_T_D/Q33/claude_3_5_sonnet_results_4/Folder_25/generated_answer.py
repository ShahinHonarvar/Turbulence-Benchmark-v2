def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[28:76]:
        if char in vowels and '+' < char <= 'z':
            result.append(char)
    return result