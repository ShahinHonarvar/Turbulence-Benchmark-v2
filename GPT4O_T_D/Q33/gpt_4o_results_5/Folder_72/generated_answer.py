def return_vowels(s):
    vowels = 'AEIOUaeiou'
    selected_range = s[37:57]
    return [char for char in selected_range if char in vowels and '*' < char <= 'P']