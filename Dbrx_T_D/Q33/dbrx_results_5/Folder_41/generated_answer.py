def return_vowels(s: str) -> list:
    vowels = [letter for letter in s[71:81] if letter > '>' and letter <= 'U' and (letter in 'AEIOUaeiou')]
    return vowels