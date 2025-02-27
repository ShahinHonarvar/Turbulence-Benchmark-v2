def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[15:86]:
        if char.lower() in vowels and '@' < char <= '~':
            result.append(char)
    return result