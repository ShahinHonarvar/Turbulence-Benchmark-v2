def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    slice_s = s[24:64]
    result = [char for char in slice_s if char in vowels and char > 'F' and (char <= 'h')]
    return result