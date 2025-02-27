def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(string) if 171 <= i < 402 and char in vowels and ('I' < char <= 'k')]