def return_vowels(s):
    return [c for c in s[1:4] if c in 'EOU' and ord(c) > ord('C')]