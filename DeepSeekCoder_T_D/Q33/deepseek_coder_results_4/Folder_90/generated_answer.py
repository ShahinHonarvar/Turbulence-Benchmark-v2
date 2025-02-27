def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[142:145] if char > s[4] and char <= 'o' and (char in vowels)]
    return result