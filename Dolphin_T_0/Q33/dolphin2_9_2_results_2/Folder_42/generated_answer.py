def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[12:39]:
        if char > ';' and char <= '|':
            if char in vowels:
                result.append(char)
    return result