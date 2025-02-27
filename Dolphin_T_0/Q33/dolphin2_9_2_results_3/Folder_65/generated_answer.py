def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[71:88] if 9 < ord(ch.lower()) <= ord('p') and ch.lower() in vowels]
    return result