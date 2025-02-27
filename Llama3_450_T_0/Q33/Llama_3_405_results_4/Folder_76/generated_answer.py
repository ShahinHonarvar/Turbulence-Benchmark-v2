def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 495 <= i < 837 and 'B' < char <= 't' and (char in vowels)]
    return result