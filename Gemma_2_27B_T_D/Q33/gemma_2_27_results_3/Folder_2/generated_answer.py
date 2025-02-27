def return_vowels(text):
    return [c for c in text[170:645] if c in 'IOU' and ord(c) > ord('E') and (ord(c) <= ord('~'))]