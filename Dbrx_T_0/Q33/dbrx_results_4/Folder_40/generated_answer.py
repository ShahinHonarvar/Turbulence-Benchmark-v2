def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[2:7]:
        if char > '^' and char <= 'd' and (char in vowels):
            result.append(char)
    return result