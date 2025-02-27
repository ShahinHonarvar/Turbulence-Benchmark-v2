def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[69:82] if char > '[' and char <= '~' and (char in vowels)]
    return result