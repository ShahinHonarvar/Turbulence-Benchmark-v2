def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[202:872] if c > s[3] and c <= s[len(s) - 1] and (c in vowels)]
    return result