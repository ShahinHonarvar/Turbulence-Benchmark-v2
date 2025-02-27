def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specified_range = s[86:99]
    result = [c for c in specified_range if 'E' < c <= 'r' and c in vowels]
    return result