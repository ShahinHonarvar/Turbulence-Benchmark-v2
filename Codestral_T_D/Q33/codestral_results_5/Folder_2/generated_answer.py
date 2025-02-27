def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[170:645] if char in vowels and 'e' < char <= '~']