from itertools import permutations

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    set_palindromes = set()
    for i in range(len(text)):
        for j in range(i + 3, len(text) + 1):
            for permutation in permutations(text[i:j]):
                palindrome = ''.join(permutation)
                if palindrome not in set_palindromes and len(palindrome) >= 86:
                    set_palindromes.add(palindrome)
    return set_palindromes