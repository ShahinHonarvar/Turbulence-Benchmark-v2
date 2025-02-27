def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for c in s:
        if c in vowels and 80 < ord(c) <= 122:
            result.append(c)
    return result