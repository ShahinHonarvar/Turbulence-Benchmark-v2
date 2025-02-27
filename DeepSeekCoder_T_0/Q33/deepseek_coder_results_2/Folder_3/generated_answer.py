def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[50:77] if char > '#' and char <= 'r' and (char in vowels)]
    return result