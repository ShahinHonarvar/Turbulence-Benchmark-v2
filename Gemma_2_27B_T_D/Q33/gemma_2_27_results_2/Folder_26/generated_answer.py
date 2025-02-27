def return_vowels(string):
    return [char for char in string[10:82] if char in 'aeiouAEIOU' and ord(char) > ord('$') and (ord(char) <= ord('@'))]