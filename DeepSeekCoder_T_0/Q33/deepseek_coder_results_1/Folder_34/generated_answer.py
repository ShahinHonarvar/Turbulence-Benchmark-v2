def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[19:32] if char > s[0] and char <= s[7] and (char in vowels)]
    return result