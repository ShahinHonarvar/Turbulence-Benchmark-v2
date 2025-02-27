def return_vowels(string):
    result = []
    for c in string[3:8]:
        if c in 'aeiouAEIOU' and c > ';' and (c <= 'D'):
            result.append(c)
    return result