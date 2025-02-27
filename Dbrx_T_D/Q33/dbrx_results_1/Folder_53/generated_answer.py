def return_vowels(s):
    vowels = [c for c in s[27:57] if 'o' < c <= 'w' and c in 'aeiouAEIOU']
    return vowels