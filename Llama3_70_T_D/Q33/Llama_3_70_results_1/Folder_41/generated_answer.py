def return_vowels(s):
    vowels = [c for c in s[71:81] if 'a' < c <= 'U' and c in 'aeiou']
    return vowels