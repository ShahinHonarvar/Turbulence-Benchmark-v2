def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_text = text[51:77]
    res = [c for c in sub_text if c in vowels and ord(c) > ord('4') and (ord(c) <= ord('='))]
    return res