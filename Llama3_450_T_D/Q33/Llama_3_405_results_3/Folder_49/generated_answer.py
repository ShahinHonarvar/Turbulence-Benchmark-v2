def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 10 <= i < 97 and 'R' < char <= 'b' and (char in vowels)]
    return result