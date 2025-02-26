def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[65:70]:
        if char in vowels and '%' < char <= 'G':
            result.append(char)
    return result