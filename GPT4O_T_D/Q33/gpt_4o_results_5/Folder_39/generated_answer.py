def return_vowels(s):
    vowels = 'AEIOUaeiou'
    start_index = 32
    end_index = 97
    return [char for char in s[start_index:end_index] if char in vowels and 'Q' < char <= ']']