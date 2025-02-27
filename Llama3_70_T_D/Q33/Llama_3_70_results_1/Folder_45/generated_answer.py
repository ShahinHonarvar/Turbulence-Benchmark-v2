def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[43:70]) if char in vowels and '*' < char <= 'b']