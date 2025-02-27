def return_vowels(s):
    return [c for c in s[32:97] if ord(c) > ord('Q') and ord(c) <= ord(']')]