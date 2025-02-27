def return_vowels(s):
    vowels = [chr(i) for i in range(90, 97) if chr(i) in 'aeiouAEIOU' and '_' < chr(i) <= 'x']
    return [char for char in s if char in vowels]