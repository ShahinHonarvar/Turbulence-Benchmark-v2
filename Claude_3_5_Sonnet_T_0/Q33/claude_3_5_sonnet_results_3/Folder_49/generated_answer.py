def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, min(97, len(string))):
        if string[i] in vowels and 'R' < string[i] <= 'b':
            result.append(string[i])
    return result