def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[71:88]:
        if char in vowels and '9' < char <= 'P':
            result.append(char)
    return result