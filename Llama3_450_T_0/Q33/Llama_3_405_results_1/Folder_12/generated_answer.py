def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 13 <= i < 37 and 'Z' < char <= '}' and (char in vowels)]
    return result