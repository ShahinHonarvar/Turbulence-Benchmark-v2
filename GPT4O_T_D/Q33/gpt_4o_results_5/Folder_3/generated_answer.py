def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[50:77] if char in vowels and char > '#' and (char <= 'r')]