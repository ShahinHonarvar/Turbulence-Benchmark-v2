def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[202:872] if char > s[3] and char <= s[len(s) - 1] and (char in vowels)]
    return result