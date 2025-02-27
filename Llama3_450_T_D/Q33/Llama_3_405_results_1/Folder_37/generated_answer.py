def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[82:90]) if char in vowels and 'T' < char <= 'b']
    return result