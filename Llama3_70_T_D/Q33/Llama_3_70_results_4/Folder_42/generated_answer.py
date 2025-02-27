def return_vowels(s):
    vowels = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) in 'aeiou']
    return [c for c in s[12:40] if c in vowels and c > ';' and (c <= '|')]