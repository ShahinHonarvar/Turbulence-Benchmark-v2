def return_vowels(s):
    vowels = [c for c in s[3:8] if 'a' < c <= 'D' and c in 'aeiouAEIOU']
    return vowels