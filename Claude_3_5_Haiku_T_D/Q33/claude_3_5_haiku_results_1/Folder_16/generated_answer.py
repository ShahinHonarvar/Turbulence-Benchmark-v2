def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(133, 306):
        if i < len(string) and string[i] in vowels and ('c' < string[i] <= 'd'):
            result.append(string[i])
    return result