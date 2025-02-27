def return_vowels(s):
    return [letter for letter in s[34:58] if letter > 'b' and letter <= 'o' and (letter.lower() in 'aeiou')]