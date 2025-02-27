def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if s[i] > '8' and s[i] <= 'F':
            if s[i].lower() in vowels:
                result.append(s[i])
    return result