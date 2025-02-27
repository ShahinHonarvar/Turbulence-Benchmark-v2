def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[10:97]:
        if 'R' < char <= 'b' and char in vowels:
            result.append(char)
    return result