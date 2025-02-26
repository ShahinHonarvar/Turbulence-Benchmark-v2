def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if i < len(s) and s[i] in vowels and (ord(s[i]) > ord('3')) and (ord(s[i]) <= ord('>')):
            result.append(s[i])
    return result