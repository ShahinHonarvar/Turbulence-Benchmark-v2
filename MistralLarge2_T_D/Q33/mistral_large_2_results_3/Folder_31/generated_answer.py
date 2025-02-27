def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 65 <= i < 70 and '%' < char <= 'G' and (char in vowels)]