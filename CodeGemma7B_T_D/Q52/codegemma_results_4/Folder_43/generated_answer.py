from collections import defaultdict
        from itertools import combinations_with_replacement

def palindrome_of_length_n(text):
    lower = text.lower()
    unique_letters = set(lower)
    max_len = (len(unique_letters) + 1) // 2
    palindromes = set()
    for i in range(max_len + 1):
        for combination in combinations_with_replacement(unique_letters, i):
            palindromes.add(''.join(sorted(i + combination + i)))
    return palindromes