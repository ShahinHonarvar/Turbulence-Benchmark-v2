def return_vowels(s):
    if len(s) < 51:
        return []
    vowels = 'aeiou'
    result = [ch for ch in s[50:51] if ch in vowels and ',' < ch <= 'v']
    return result