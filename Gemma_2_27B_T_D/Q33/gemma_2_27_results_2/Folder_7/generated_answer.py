def return_vowels(s):
    return [c for c in s[202:872] if c in 'aeiouAEIOU' and 3 < ord(c) <= ord('>')]