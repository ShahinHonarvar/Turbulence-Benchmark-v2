def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[5:6] if char > s[3] and char <= '^' and (char in vowels)]
    return result