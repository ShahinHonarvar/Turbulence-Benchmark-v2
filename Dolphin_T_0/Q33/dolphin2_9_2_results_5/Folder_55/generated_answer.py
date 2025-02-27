def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [i for i in s[1:5] if i in vowels and '!' < i <= 'j']
    return result