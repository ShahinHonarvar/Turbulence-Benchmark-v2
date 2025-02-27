import re
  from collections import Counter

def palindromes_between_indices(string):
    string = string[3:9]
    letters = re.findall('[a-zA-Z]', string)
    letters = [letter.lower() for letter in letters]
    letter_counts = Counter(letters)
    palindromes = set()
    if len(letters) >= 6:
        for letter in letter_counts:
            if letter_counts[letter] >= 3:
                palindrome = letter * 3
                palindromes.add(palindrome)
        for i in range(len(letters) - 1):
            for j in range(i + 1, len(letters)):
                if letters[i] != letters[j]:
                    for k in range(len(letters)):
                        if k != i and k != j:
                            palindrome1 = letters[i] + letters[j] + letters[k] * 2 + letters[j] + letters[i]
                            palindrome2 = letters[j] + letters[i] + letters[k] * 2 + letters[i] + letters[j]
                            palindromes.add(palindrome1)
                            palindromes.add(palindrome2)
    return palindromes