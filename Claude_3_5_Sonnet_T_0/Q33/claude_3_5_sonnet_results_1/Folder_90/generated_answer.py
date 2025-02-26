def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[142:145]:
        if char in vowels and '4' < char <= 'o':
            result.append(char)
    return result