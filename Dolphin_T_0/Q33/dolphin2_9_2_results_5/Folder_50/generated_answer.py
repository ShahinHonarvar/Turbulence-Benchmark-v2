def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    match = [x for x in s[11:53] if x > '+' and x <= 'W' and (x in vowels)]
    return match