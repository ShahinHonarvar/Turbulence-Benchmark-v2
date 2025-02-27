def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[142:145], start=142) if char in vowels and ord('4') < ord(char) <= ord('o')]