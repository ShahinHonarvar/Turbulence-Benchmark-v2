def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(70, 76):
        if i < len(s):
            char = s[i]
            if char in vowels and '2' < char <= ':':
                result.append(char)
    return result