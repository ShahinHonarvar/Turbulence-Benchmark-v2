def return_vowels(s):
    vowels = set('AEIOUaeiou')
    result = []
    for char in s[20:34]:
        if char in vowels and 'U' < char <= 'i':
            result.append(char)
    return result