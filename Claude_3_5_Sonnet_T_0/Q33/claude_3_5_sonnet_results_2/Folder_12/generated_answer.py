def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[13:37]:
        if char in vowels and 'Z' < char <= '}':
            result.append(char)
    return result