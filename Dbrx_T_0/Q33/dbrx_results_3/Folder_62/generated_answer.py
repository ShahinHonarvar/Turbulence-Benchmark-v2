def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[14:60]:
        if char.lower() in vowels and 'D' < char <= 'v':
            result.append(char)
    return result