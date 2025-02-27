def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[69:82]:
        if char >= 'a' and char <= '~':
            result.append(char)
    return result