def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[71:88]:
        if '9' < char <= 'P' and char in vowels:
            result.append(char)
    return result