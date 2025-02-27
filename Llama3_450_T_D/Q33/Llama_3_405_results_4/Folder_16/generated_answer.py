def return_vowels(s):
    vowels = 'aeiouAEIOU'
    c = 'c'
    d = 'd'
    result = [char for i, char in enumerate(s) if 133 <= i < 306 and c < char <= d and (char in vowels)]
    return result