def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[12:39]) if char.lower() in vowels and ';' < char <= '|']