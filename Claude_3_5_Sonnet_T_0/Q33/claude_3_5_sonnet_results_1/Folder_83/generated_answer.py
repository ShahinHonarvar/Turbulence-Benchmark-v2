def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[90:97]:
        if char in vowels and '_' < char <= 'x':
            result.append(char)
    return result