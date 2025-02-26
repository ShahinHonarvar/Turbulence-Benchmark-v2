def return_vowels(s):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [char for char in s[51:77] if char in vowels and '4' < char <= '=']
    return filtered_vowels