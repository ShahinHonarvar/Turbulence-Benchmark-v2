def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[34:69]) if char.lower() in vowels and '_' < char.lower() <= 'o']