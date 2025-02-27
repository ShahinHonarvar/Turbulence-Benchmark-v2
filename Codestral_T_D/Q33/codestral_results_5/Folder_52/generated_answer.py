def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[24:68]:
        if char in vowels and 'f' < char <= '|':
            result.append(char)
    return result