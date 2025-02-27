def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 149 <= i < 313 and 'M' < char <= 'j' and (char in vowels)]
    return result