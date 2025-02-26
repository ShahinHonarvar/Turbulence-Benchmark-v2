def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if i < len(s):
            char = s[i]
            if char in vowels and ord(char) > ord('3') and (ord(char) <= ord('>')):
                result.append(char)
    return result