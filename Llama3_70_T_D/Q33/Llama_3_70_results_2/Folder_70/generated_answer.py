def return_vowels(s):
    vowels = [c for c in s[171:402] if 'I' < c <= 'k' and c in 'aeiou']
    return vowels