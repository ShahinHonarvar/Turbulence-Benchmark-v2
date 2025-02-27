def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if char in vowels and 46 <= i < 90 and (char > '@') and (char <= '[')]