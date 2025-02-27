def return_vowels(s):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s[170:645]:
        if 'E' < char <= '~':
            if char.lower() in vowels:
                result.append(char)
    return result