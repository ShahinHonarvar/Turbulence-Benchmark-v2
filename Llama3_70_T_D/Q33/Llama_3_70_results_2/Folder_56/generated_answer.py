def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[15:86], 15) if char in vowels and '@' < char <= '~']