def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(20, 41):
        if i < len(s):
            char = s[i].upper()
            if char in vowels and 'K' < char <= 'Z':
                result.append(char)
    return result