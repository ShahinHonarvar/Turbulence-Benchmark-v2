def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[1:9]:
        if char in vowels and char > '?' and (char <= 'k'):
            result.append(char)
    return result