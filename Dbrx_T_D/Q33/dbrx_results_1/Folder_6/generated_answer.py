def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[20:34]) if char.lower() in vowels and 'u' < char.lower() <= 'i']