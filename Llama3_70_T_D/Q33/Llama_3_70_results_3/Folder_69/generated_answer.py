def return_vowels(s):
    vowels = [c for c in s[641:872] if 'a' < c <= 'q' and c in 'aeiou']
    return vowels