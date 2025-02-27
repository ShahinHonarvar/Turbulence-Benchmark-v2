def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 1 <= i < 5 and '!' < char <= 'j' and (char in vowels)]
    return result