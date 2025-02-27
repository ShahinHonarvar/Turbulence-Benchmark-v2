def return_vowels(s):
    vowels = 'aeiou'
    if len(s) > 50:
        return [char for char in s[50:51] if char in vowels and ',' < char <= 'v']
    return []