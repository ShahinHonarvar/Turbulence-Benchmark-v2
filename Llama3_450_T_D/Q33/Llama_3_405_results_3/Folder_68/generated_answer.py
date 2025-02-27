def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[1:9]) if char in vowels and '?' < char <= 'k']