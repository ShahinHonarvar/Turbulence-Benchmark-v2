def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[20:34]:
        if 'u' < char <= 'i' and char in vowels:
            result.append(char)
    return result