def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for index, char in enumerate(s) if 47 <= index < 89 and '@' < char <= 'n' and (char in vowels)]
    return result