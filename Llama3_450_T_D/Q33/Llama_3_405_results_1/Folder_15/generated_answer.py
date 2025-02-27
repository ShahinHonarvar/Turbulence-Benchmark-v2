def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[5:6]:
        if char in vowels and ord(char) > 51 and (ord(char) <= 94):
            result.append(char)
    return result