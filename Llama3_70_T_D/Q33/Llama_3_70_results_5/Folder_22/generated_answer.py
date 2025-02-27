def return_vowels(s):
    vowels = [chr(i) for i in range(97, 123) if chr(i) in 'aeiou']
    return [v for v in vowels if 'K' < v <= 'z' and s.find(v) >= 56 and (s.find(v) < 90)]