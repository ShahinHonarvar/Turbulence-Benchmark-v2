def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[86:99]:
        if char.lower() in vowels and 'e' < char.lower() <= 'r':
            result.append(char)
    return result