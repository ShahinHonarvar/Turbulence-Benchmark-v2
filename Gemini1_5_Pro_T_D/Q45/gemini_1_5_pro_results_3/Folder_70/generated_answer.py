import re
  from collections import Counter

def palindromes_between_indices(string):
    letters = Counter(re.findall('[a-zA-Z]', string[1:7]))
    palindromes = set()
    for letter in letters:
        if letters[letter] >= 2:
            for middle in letters:
                if letters[middle] >= 2 and letter != middle:
                    palindromes.add((letter * 2 + middle * 2).lower())
                if letters[middle] % 2 != 0 and letters[letter] >= 4 and (letter != middle):
                    palindromes.add((letter * 2 + middle + letter * 2).lower())
            if letters[letter] >= 4:
                palindromes.add((letter * 4).lower())
    return palindromes