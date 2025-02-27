def return_vowels(s):
    result = []
    for char in s[82:90]:
        if char > 'T' and char <= 'b':
            if char.lower() in 'aeiou':
                result.append(char)
    return result