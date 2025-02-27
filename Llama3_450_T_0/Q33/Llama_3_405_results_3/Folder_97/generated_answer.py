def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 328 <= i < 455 and '<' < char <= 'z' and (char in vowels)]
    return result