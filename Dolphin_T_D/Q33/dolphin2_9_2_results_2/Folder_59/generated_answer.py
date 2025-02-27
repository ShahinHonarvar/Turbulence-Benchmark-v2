def return_vowels(s):
    upper_bound = s[9] if 9 < len(s) else ''
    lower_bound = s[8]
    vowels = 'aeiou'
    result_list = [ch for ch in s[8:9] if ch in vowels and ch > 'Y' and (ch <= upper_bound)]
    return result_list