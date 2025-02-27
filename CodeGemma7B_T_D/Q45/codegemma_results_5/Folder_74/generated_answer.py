from itertools import permutations

def palindromes_between_indices(text):
    lowercase_text = text.lower()
    letters_in_range = [char for char in lowercase_text if 1 <= len(char) <= 6 and char.isalpha()]
    palindrome_set = set()
    for length in range(6, 0, -1):
        for permutation in permutations(letters_in_range, length):
            palindrome_candidate = ''.join(permutation)
            if palindrome_candidate == palindrome_candidate[::-1]:
                palindrome_set.add(palindrome_candidate)
    return palindrome_set