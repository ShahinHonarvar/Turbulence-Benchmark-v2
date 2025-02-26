def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(323, 526):
        if i < len(s):
            char = s[i]
            if char in vowels and '+' < char <= ':':
                result.append(char)
    return result