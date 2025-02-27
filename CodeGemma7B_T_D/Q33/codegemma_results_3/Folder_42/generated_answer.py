def return_vowels(string):
    vowels = [i for i in string[12:39] if i in 'aeiouAEIOU' and ord(i) > ord(';') and (ord(i) <= ord('|'))]
    return vowels if vowels else []