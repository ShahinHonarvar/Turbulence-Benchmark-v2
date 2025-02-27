import re
  from collections import Counter

def palindromes_between_indices(string):
    string = string[6:10]
    letters = re.findall('[a-zA-Z]', string)
    letters = [letter.lower() for letter in letters]
    letter_counts = Counter(letters)
    palindromes = set()
    for letter in letter_counts:
        if letter_counts[letter] >= 2:
            for other_letter in letter_counts:
                if other_letter != letter and letter_counts[other_letter] >= 2:
                    palindrome = letter * 2 + other_letter * 2 + letter * 2
                    palindromes.add(palindrome)
    return palindromes