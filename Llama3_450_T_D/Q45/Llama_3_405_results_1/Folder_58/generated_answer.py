import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(6, len(s) + 1):
        for combo in itertools.combinations_with_replacement(letters, r // 2):
            first_half = ''.join(combo)
            palindrome = first_half + (first_half[::-1] if r % 2 == 0 else first_half[::-1][1:])
            if all((letter_count(palindrome, letter) <= letter_count(s, letter) for letter in letters)):
                palindromes.add(palindrome)
    return palindromes

def letter_count(s, letter):
    return sum((1 for char in s if char == letter))