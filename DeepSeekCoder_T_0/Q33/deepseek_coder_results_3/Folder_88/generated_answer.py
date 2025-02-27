def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[70:76] if char > s[2] and char <= ':' and (char in vowels)]
    return result