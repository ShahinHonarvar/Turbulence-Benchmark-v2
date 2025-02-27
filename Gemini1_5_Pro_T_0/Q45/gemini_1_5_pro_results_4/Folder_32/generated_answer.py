from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:8].lower()
    letters = [letter for letter in string if letter.isalpha()]
    palindrome_set = set()
    if len(letters) < 5:
        return palindrome_set
    letter_counts = Counter(letters)
    odd_counts = [letter for letter, count in letter_counts.items() if count % 2 == 1]
    if len(odd_counts) > 1:
        return palindrome_set
    middle_letter = ''
    if len(odd_counts) == 1:
        middle_letter = odd_counts[0]
        letter_counts[middle_letter] -= 1
    half_palindrome = ''
    for letter, count in letter_counts.items():
        half_palindrome += letter * (count // 2)
    for permutation in permutations(half_palindrome):
        palindrome = ''.join(permutation) + middle_letter + ''.join(permutation[::-1])
        palindrome_set.add(palindrome)
    return palindrome_set