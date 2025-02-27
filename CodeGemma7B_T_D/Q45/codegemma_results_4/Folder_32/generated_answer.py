from itertools import product

def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_s = s[1:7].lower()
    palindromes = set()
    if not filtered_s:
        return set()
    for length in range(5, len(filtered_s) + 1):
        for combination in product(letters, repeat=length):
            candidate_palindrome = ''.join(combination)
            if candidate_palindrome in filtered_s:
                palindromes.add(candidate_palindrome)
    return palindromes