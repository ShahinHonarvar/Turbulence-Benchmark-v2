def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[163:771] if char > ':' and char <= 'E' and (char in vowels)]
    return result