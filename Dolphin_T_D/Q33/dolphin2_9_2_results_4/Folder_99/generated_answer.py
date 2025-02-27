def return_vowels(s):
    result = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(323, 526):
        char = s[i]
        if '+' < char <= ':' and char in vowels:
            result.append(char)
    return result