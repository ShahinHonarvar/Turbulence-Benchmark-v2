def return_vowels(s):
    vowels = 'AEIOU'
    result = [chr(i) for i in range(65, 70) if chr(i) > '%' and chr(i) <= 'G' and (chr(i) in vowels)]
    return result