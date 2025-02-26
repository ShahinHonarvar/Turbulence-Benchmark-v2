def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[41:50]:
        if char in vowels and 'W' < char <= '[':
            result.append(char)
    return result