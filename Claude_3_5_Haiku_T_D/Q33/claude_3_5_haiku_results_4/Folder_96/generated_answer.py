def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(77, 84):
        if i < len(s):
            char = s[i]
            if char in vowels and ord('(') < ord(char) <= ord('G'):
                result.append(char)
    return result