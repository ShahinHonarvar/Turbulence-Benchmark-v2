def return_vowels(s):
    vowels = 'aeiou'
    temp_list = [s[i] for i in range(12, 39) if s[i] > ';' and s[i] <= '|']
    return [char for char in temp_list if char in vowels]