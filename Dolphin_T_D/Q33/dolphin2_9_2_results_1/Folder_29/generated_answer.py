def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[19:20]:
        if char > '<' and char <= 'p':
            if char in vowels:
                result.append(char)
    return result