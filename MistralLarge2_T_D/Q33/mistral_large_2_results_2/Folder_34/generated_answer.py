def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[19:32]) if char in vowels and '0' < char <= '7']