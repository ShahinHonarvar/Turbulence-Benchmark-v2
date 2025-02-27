def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[51:77] if char > '4' and char <= '=' and (char in vowels)]
    return result