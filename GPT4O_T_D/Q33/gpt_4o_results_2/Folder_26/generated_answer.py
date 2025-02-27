def return_vowels(s):
    result = []
    for char in s[10:82]:
        if char in 'AEIOUaeiou' and '$' < char <= '@':
            result.append(char)
    return result