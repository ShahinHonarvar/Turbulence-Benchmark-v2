def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(5, 6):
        if i < len(string) and string[i] in vowels and ('3' < string[i] <= '^'):
            result.append(string[i])
    return result