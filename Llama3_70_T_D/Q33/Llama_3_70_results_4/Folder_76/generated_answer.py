def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(string[495:837], 495) if char in vowels and 'B' < char <= 't']