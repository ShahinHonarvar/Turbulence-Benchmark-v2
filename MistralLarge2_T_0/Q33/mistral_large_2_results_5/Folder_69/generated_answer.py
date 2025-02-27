def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[641:872] if char in vowels and '>' < char <= 'q']