def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_range = s[85:99]
    result = [x for x in specified_range if x > '/' and x <= 'n' and (x in vowels)]
    return result