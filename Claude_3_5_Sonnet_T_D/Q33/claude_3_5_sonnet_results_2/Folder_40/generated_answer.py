def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[2:7]:
        if char in vowels and '^' < char <= 'd':
            result.append(char)
    return result