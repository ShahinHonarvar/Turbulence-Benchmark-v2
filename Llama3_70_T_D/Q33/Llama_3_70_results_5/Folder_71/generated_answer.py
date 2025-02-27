def return_vowels(s):
    vowels = [c for c in s[36:56] if '+' < c <= '/']
    vowels = [c for c in vowels if c in 'aeiouAEIOU']
    return vowels