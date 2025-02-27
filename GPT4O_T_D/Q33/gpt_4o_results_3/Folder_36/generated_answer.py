def return_vowels(s):
    vowels = set('aeiouAEIOU')
    result = [ch for ch in s[604:949] if ch in vowels and 'N' < ch <= 'U']
    return result