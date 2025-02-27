def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    return [char for char in set(s[34:58]) if char in vowels and 'b' < char <= 'o']