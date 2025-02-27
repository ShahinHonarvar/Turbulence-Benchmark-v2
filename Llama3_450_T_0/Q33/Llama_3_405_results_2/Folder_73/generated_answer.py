def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 47 <= i < 89 and '@' < char <= 'n' and (char in vowels)]
    return result