def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[70:76] if ch in vowels and ord(ch) > ord('2') and (ord(ch) <= ord(':'))]