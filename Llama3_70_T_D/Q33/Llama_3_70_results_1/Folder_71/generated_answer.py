def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[36:56]) if c in vowels and '+' < c <= '/']