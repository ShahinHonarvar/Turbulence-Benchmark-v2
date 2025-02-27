def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[51:77]:
        if char in vowels and 4 < ord(char) <= ord('='):
            result.append(char)
    return result