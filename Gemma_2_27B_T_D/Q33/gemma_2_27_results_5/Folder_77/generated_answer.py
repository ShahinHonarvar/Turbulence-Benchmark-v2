def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[837:975] if c in vowels and c > 'N' and (c <= 'W')]