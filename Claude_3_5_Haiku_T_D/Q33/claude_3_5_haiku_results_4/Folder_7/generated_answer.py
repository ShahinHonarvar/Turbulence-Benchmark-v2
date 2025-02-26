def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[202:872] if char in vowels and '3' < char <= '>']
    return result