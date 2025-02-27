def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[24:64]:
        if char > 'F' and char <= 'h' and (char in vowels):
            result.append(char)
    return result