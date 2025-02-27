def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s if ord(c) >= ord('Q') and ord(c) < ord(']') and (c in vowels)]
    return result