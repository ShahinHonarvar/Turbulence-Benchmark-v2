def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(32, 61):
        if i < len(string):
            char = string[i]
            if char in vowels and '?' < char <= 'P':
                result.append(char)
    return result