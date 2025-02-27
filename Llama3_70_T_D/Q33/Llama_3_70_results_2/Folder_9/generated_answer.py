def return_vowels(s):
    vowels = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) in 'aeiou']
    return [c for i, c in enumerate(s[13:36], 13) if c in vowels and ord(c) > 8 and (ord(c) <= ord('F'))]