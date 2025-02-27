def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 40 <= i < 94 and '4' < char <= 'H' and (char in vowels)]
    return result