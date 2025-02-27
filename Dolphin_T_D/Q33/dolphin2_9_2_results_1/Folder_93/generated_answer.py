def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(54, 82):
        if '@' >= s[i] > '=':
            if s[i].lower() in vowels:
                result.append(s[i].lower())
    return result