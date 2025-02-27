def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[70:76]:
        if char in vowels and char > '2' and (char <= ':'):
            result.append(char)
    return result