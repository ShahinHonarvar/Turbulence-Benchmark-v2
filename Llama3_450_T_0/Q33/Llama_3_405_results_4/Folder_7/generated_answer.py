def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[202:872]) if char in vowels and char > '3' and (char <= '>')]
    return result