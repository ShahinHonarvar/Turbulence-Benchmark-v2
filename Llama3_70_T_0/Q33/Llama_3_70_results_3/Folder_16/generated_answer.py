def return_vowels(s, c, d):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[133:306], 133) if char in vowels and c < char <= d]