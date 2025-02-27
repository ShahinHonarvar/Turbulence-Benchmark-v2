def return_vowels(s):
    result = []
    for i in range(202, 872):
        if s[i] in 'aeiouAEIOU' and 3 < ord(s[i]) <= ord('>'):
            result.append(s[i])
    return result