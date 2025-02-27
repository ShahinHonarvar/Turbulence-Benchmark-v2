def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = [i for i in string[59:61] if i in vowels and ord(i) + 1 < ord('h')]
    return res or []