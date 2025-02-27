def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[163:771]:
        if ':' < char <= 'E':
            if char.lower() in vowels:
                result.append(char)
    return result