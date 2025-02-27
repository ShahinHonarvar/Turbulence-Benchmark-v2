def return_vowels(s, c, d):
    vowels = 'aeiouAEIOU'
    indices = s[133:306]
    filtered_vowels = [x.lower() for x in indices if c < x.lower() <= d and x.lower() in vowels]
    return filtered_vowels