def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[1:7]:
        if char.lower() in vowels and 'F' < char <= 'j':
            result.append(char)
    return result