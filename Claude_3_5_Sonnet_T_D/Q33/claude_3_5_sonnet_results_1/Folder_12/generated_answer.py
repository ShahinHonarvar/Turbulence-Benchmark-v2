def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 37):
        if i < len(string):
            if string[i] in vowels and 'Z' < string[i] <= '}':
                result.append(string[i])
    return result