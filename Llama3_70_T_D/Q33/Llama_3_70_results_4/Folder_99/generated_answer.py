def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(323, 526):
        if len(s) > i:
            if s[i] > '+' and s[i] <= ':' and (s[i] in vowels):
                result.append(s[i])
    return result