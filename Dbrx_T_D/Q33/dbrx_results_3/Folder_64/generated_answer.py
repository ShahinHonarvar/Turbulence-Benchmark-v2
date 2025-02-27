def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [v for v in s[1:7] if v.lower() > 'f' and v.lower() <= 'j' and (v in vowels)]
    return result