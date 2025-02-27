def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_range = s[464:574]
    result = [c for c in specified_range if c in vowels and c > 'a' and (c <= 'g')]
    return result