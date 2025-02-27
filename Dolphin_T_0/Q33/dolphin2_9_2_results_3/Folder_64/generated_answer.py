def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ret = [s[i] for i in range(1, 7) if s[i].lower() in vowels and 'f' < s[i].lower() <= 'j']
    return ret