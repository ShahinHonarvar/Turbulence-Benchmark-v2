def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(32, 97):
        if i < len(string):
            char = string[i]
            if char in vowels and 'Q' < char <= ']':
                result.append(char)
    return result