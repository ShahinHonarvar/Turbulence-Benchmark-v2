def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 23 <= i < 38 and 'N' < char <= 'k' and (char in vowels)]
    return result