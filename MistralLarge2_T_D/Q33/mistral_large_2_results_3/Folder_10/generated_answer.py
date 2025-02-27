def return_vowels(s):
    vowels = set('aeiouAEIOU')
    result = [char for char in s[31:37] if char > ';' and char <= 't' and (char in vowels)]
    return result