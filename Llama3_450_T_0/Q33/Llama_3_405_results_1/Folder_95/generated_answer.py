def return_vowels(s):
    vowels = 'AEIO'
    result = [char for i, char in enumerate(s) if 32 <= i < 61 and '?' < char <= 'P' and (char in vowels)]
    return result