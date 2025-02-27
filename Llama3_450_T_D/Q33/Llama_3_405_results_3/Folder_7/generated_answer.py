def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, min(872, len(s))):
        if s[i] in vowels and s[i] > chr(3) and (s[i] <= chr(ord(s[i]))):
            result.append(s[i])
    return result