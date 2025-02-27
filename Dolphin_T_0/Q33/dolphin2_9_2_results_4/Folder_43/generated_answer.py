def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for c in s[22:82]:
        if c > 'N' and c <= 'o' and (c in vowels):
            result.append(c)
    return result