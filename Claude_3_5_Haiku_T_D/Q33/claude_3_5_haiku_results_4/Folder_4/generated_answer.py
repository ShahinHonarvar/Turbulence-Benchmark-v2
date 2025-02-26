def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 91):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'a' < char <= 'x':
                result.append(char)
    return result