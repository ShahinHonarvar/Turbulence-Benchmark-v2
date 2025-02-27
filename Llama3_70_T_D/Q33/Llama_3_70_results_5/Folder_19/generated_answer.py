def return_vowels(s):
    vowels = [s[i] for i in range(51, 77) if 4 < ord(s[i]) <= ord('=') and s[i].lower() in 'aeiou']
    return vowels