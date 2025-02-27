def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 60 <= i < 99 and 'j' < char <= 'n' and (char in vowels)]
    return result