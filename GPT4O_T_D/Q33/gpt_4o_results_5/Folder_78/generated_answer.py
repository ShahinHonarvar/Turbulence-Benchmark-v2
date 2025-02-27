def return_vowels(s):
    if len(s) < 46:
        return []
    vowels = 'aeiouAEIOU'
    vowel_list = [char for char in s[46:90] if char in vowels if '@' < char <= '[']
    return vowel_list