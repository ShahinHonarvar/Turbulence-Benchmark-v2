def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[47:61] if char > '9' and char <= 'O' and (char in vowels)]
    return result