def return_vowels(s):
    vowels = [chr(i) for i in range(ord('+') + 1, ord(':') + 1) if chr(i) in 'aeiouAEIOU']
    return [char for char in s[323:526] if char in vowels]