def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [vowel for vowel in vowels if string.find(vowel) >= 202 and string.find(vowel) < 872 and (string[string.find(vowel)] > '3') and (string[string.find(vowel)] <= '>')]
    return result if result else []