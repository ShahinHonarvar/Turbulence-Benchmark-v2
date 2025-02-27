def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_string = s[22:82]
    res = [ch for ch in sub_string if 'n' < ch <= 'o' and ch in vowels]
    return res