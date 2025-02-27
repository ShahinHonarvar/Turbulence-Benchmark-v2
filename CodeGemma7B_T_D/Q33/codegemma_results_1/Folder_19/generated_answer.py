def return_vowels(string):
    vowels = []
    for vowel in string[51:77].lower():
        if vowel in 'aeiouAEIOU' and 4 < ord(vowel) <= ord('=') and (vowel not in vowels):
            vowels.append(vowel)
    return vowels