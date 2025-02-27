def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[71:88]:
        if char > '9' and char <= 'P':
            if char in vowels:
                result.append(char)
    return result