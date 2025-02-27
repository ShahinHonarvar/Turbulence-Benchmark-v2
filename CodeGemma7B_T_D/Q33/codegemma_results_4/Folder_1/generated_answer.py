def return_vowels(s):
    result = []
    for i in range(24, 64):
        if s[i] in 'aeiouAEIOU' and ord(s[i]) > ord('F') and (ord(s[i]) <= ord('h')):
            result.append(s[i])
    return result