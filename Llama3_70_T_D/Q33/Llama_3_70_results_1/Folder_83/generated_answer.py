def return_vowels(s):
    vowels = [chr(i) for i in range(97, 123) if chr(i) in 'aeiou']
    return [c for c in s[90:97] if c > '_' and c <= 'x' and (c in vowels)]