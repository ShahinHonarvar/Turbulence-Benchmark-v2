def return_vowels(user_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    user_string = user_string.lower()
    filtered_vowels = [vowel for vowel in user_string[31:37] if vowel in vowels and vowel > ';' and (vowel <= 't')]
    return filtered_vowels