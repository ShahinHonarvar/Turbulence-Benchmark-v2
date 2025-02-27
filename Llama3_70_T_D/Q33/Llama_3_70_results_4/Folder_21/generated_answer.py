def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 464 <= i < 574 and 'a' < char <= 'g' and (char in 'aeiou')]
    return vowels