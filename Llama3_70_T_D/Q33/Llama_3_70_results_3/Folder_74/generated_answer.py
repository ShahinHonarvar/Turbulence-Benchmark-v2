def return_vowels(s):
    vowels = [chr(i) for i in range(69, 82) if chr(i) > '[' and chr(i) <= '~' and (chr(i) in 'aeiouAEIOU')]
    return [char for char in vowels if char in s]