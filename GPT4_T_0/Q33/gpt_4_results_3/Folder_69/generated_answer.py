def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in s[641:872] if char in vowels and '>' < char <= 'q']
    return result