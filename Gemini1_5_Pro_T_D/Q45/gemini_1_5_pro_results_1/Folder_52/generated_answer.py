from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((char for char in string[:8] if char.lower() in english_letters)).lower()
    char_counts = Counter(filtered_string)
    palindromes = set()
    for i in range(6, len(filtered_string) + 1):
        for permutation in permutations(filtered_string, i):
            potential_palindrome = ''.join(permutation)
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome not in palindromes:
                char_counts_permutation = Counter(potential_palindrome)
                if all((char_counts_permutation[char] <= char_counts[char] for char in char_counts_permutation)):
                    palindromes.add(potential_palindrome)
    return palindromes