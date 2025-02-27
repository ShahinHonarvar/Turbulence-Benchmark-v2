def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[19:32] if char in vowels and s[0] < char <= s[7]]
    return result