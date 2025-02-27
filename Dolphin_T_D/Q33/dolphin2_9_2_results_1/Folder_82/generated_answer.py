def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[86:99]:
        if char in vowels and char > 'E' and (char <= 'r'):
            result.append(char)
    return result