def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 529 <= i < 828 and char in vowels and ('U' < char <= 'l')]