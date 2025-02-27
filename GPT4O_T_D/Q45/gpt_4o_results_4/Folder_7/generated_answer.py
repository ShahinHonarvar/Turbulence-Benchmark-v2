from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:10].lower()
    letter_freq = Counter([c for c in substr if c.isalpha()])
    potential_chars = ''.join((char * (count // 2 * 2) for char, count in letter_freq.items()))
    palindromes = set()
    for half in set(permutations(potential_chars, 3)):
        half = ''.join(half)
        middle_chars = [char for char, count in letter_freq.items() if count % 2 == 1]
        if middle_chars:
            for middle in middle_chars:
                palindrome = half + middle + half[::-1]
                if len(palindrome) >= 7:
                    palindromes.add(palindrome)
        else:
            palindrome = half + half[::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes