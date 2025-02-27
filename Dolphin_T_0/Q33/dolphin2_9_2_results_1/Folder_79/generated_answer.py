def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[74:96] if ch.lower() in vowels and ch.lower() > 'i' and (ch.lower() <= 'x')]