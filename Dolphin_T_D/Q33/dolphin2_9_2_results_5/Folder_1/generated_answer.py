def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[24:64] if ch.lower() in vowels and ch.lower() > 'f' and (ch.lower() <= 'h')]