def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[202:872] if char in vowels and char > '3' and (char <= '>')]
    return result