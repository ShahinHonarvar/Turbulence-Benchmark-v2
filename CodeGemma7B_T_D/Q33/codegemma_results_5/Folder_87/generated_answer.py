def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return_list = []
    for i in range(len(s)):
        if i >= 34 and i < 58 and (s[i] in vowels) and (ord(s[i]) > ord('b')) and (ord(s[i]) <= ord('o')):
            return_list.append(s[i])
    return return_list