def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[44:95]:
        if char > '5' and char <= '<' and (char in vowels):
            result.append(char)
    return result