def return_vowels(s):
    vowels = [chr(i) for i in range(97, 123) if chr(i) in 'aeiou']
    return [i for i in s[34:58] if i in vowels and 'b' < i <= 'o']