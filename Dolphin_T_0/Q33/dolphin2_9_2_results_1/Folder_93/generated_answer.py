def return_vowels(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[54:82]:
        if '`' < char <= '@' and char.lower() in vowels_list:
            result.append(char)
    return result