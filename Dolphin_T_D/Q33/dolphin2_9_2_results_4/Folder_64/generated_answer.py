def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[1:7]:
        if 'f' < char <= 'j' and char in vowels:
            result.append(char)
    return result