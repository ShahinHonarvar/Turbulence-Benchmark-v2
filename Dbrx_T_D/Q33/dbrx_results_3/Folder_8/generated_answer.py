def return_vowels(s):
    vowels = [i for i in s if ord('P') < ord(i) <= ord('z') and ord(i) < 82 and (64 <= ord(i)) for i in s if i in 'AEIOUaeiou']
    return vowels