def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(54, 82):
        if i < len(string):
            char = string[i]
            if char in vowels and '=' < char <= '@':
                result.append(char)
    return result