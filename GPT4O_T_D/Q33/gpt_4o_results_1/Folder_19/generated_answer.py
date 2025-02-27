def return_vowels(s):
    if len(s) < 52:
        return []
    vowels = 'aeiouAEIOU'
    valid_range = s[51:77]
    result = [char for char in valid_range if char in vowels and '4' < char <= '=']
    return result