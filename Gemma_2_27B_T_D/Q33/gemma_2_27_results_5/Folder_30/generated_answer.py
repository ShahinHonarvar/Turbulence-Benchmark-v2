def return_vowels(string):
    return [c for c in string[11:61] if c in 'aeiouAEIOU' and ord('M') < ord(c) <= ord('W')]