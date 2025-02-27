def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[323:526] if c in vowels and '+' < c <= ':']
    return result