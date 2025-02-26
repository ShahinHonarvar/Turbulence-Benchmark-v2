def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, 97):
        if i < len(string) and string[i] in vowels and (string[i] > 'R') and (string[i] <= 'b'):
            result.append(string[i])
    return result