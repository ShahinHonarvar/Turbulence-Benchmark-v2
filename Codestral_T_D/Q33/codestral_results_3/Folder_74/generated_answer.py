def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in str[69:82] if char in vowels and '[' < char <= '~']