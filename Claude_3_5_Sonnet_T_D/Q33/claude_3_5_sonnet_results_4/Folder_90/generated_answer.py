def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[142:145]:
        if char in vowels and '4' < char <= 'o':
            result.append(char)
    return result