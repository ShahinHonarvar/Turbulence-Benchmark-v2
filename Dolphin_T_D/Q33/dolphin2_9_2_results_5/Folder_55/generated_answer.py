def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub = s[1:5]
    res = [char for char in sub if char in vowels and '!' < char <= 'j']
    return res