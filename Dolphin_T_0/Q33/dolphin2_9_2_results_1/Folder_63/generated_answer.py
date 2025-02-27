def return_vowels(s):
    vowels = 'aeiou'
    result = [s[i] for i in range(34, 69) if s[i] in vowels and s[i] > '_' and (s[i] <= 'o')]
    return result if result else []