def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[15:86] if char in vowels and '@' < char <= '~']
    return result