def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[10:97] if char.lower() > 'r' and char.lower() <= 'b' and (char.lower() in vowels)]
    return result