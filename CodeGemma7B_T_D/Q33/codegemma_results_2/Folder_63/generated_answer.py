def return_vowels(s):
    return [c for c in ''.join([y.lower() for y in ''.join(s).split()]) if 97 <= ord(c) <= 111 and c > '_' and (c <= 'o') and (34 <= s.index(c) < 69)]