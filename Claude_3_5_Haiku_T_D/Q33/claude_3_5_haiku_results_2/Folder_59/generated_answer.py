def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[8:9]:
        if char in vowels and 'Y' < char <= 's':
            result.append(char)
    return result