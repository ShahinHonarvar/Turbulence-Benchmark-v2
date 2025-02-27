def return_vowels(s):
    vowels = 'aeiouAEIOU'
    if len(s) > 8:
        return [char for char in s[8:9] if char in vowels and 'Y' < char <= 's']
    return []