from string import ascii_lowercase

def return_vowels(s):
    vowels = list(filter(lambda x: x in ascii_lowercase and ord(x) > ord('a') and (ord(x) <= ord('g')) and (s.index(x) >= 464) and (s.index(x) < 574), s))
    return vowels or []