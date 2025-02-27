def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[163:771] if char in vowels and ':' < char <= 'E']