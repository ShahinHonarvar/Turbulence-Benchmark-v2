def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 68):
        if i < len(string):
            char = string[i]
            if char in vowels and 'f' < char <= '|':
                result.append(char)
    return result