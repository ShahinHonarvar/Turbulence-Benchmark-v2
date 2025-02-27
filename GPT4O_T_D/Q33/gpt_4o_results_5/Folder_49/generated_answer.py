def return_vowels(s):
    if len(s) < 10:
        return []
    vowels = 'aeiouAEIOU'
    filtered_vowels = [char for char in s[10:97] if char in vowels and 'R' < char <= 'b']
    return filtered_vowels