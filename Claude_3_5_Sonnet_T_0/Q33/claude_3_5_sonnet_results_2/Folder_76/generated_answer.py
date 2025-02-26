def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(495, 837):
        if i < len(string):
            char = string[i]
            if char in vowels and 'B' < char <= 't':
                result.append(char)
    return result