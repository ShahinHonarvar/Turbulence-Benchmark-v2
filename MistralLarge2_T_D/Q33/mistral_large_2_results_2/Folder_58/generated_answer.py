def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 260 <= i < 322 and '%' < char <= 'U' and (char in vowels)]