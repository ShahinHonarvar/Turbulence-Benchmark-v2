def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[464:574] if c in vowels and 'a' < c <= 'g']
    return result