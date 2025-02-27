import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7].lower()))
    letters = sorted(set(s))
    palindromes = set()
    for r in range(6, len(s) + 1):
        for combo in itertools.combinations_with_replacement(letters, r // 2):
            first_half = ''.join(combo)
            palindrome = first_half + first_half[::-1]
            if r % 2 == 1:
                for letter in letters:
                    palindrome = first_half + letter + first_half[::-1]
                    if all((palindrome.count(c) <= s.count(c) for c in letters)):
                        palindromes.add(palindrome)
            elif all((palindrome.count(c) <= s.count(c) for c in letters)):
                palindromes.add(palindrome)
    return palindromes