def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(15, 86):
        try:
            char = s[i]
            if char in vowels and '@' < char <= '~':
                result.append(char)
        except IndexError:
            break
    return result