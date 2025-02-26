def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(528, 606):
        if i < len(s):
            char = s[i]
            if char in vowels and 'M' < char <= 'X':
                result.append(char)
    return result