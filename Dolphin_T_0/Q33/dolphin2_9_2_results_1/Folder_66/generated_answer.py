def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_str = s[63:79]
    result = [char for char in sub_str if char in vowels and 'd' < char <= 'y']
    return result