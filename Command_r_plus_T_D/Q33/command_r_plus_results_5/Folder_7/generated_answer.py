def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for ch in s[202:872] if ch in vowels and ord(ch) > 3 and (ord(ch) <= 62)]
    return result