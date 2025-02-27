def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for idx, char in enumerate(s) if 47 <= idx < 89 and '@' < char <= 'n' and (char in vowels)]
    return result