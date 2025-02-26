def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[19:32] if char in vowels and '0' < char <= '7']