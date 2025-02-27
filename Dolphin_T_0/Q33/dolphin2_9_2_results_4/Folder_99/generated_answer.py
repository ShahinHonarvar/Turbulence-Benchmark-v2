def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[323:526] if c in vowels and '+' < c <= ':']
    return result