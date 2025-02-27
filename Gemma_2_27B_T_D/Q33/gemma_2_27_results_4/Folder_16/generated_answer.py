def return_vowels(s):
    return [letter for letter in s[133:306] if letter in 'aeiouAEIOU' and letter > 'c' and (letter <= 'd')]