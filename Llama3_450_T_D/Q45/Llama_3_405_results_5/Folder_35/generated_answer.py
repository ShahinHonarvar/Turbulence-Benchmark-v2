from collections import Counter
    import itertools

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    english_letters = [char for char in s[2:5].lower() if char.isalpha()]
    letter_counts = Counter(english_letters)
    palindromes = set()
    for r in range(4, sum(letter_counts.values()) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            if is_palindrome(combo):
                palindrome = ''.join(combo)
                palindromes.add(palindrome)
    return palindromes