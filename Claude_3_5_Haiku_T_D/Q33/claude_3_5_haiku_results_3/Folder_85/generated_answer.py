def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'z' < char <= 'w':
                result.append(s[i])
    return result