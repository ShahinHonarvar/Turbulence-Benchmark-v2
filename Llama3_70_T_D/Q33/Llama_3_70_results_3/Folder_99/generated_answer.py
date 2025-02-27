def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[323:526], 323) if c in vowels and '+' < c <= ':']