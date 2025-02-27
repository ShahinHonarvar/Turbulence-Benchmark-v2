def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[44:95]:
        if 5 < ord(char) <= ord('<') and char in vowels:
            result.append(char)
    return result