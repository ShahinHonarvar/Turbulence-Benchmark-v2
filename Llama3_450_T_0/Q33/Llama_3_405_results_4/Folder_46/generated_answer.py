def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 10 <= i < 83 and '%' < char <= 'e' and (char in vowels)]
    return result