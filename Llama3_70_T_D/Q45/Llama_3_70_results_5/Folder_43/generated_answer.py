from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(input_string):
    input_string = input_string.lower()
    substring = input_string[2:6]
    english_letters = [char for char in substring if char in ascii_lowercase]
    unique_english_letters = set(english_letters)
    if len(unique_english_letters) < 2:
        return set()
    palindromes = set()
    for letter1 in unique_english_letters:
        for letter2 in unique_english_letters:
            if letter1 != letter2:
                for letter3 in unique_english_letters:
                    for letter4 in unique_english_letters:
                        if letter3 != letter4 and (letter1, letter2) != (letter4, letter3):
                            palindrome = letter1 + letter2 + letter3 + letter4 + letter3 + letter2 + letter1
                            palindromes.add(palindrome)
    return palindromes