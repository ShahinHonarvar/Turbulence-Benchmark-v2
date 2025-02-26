def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(604, 949):
        if i < len(s):
            char = s[i]
            if char in vowels and 'N' < char <= 'U':
                result.append(char)
    return result