def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[202:872], 202) if char in vowels and char > '3' and (char <= '>')]