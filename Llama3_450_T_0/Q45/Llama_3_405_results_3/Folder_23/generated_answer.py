import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for combo in itertools.combinations_with_replacement(letters, r // 2):
            first_half = ''.join(combo)
            if r % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                for letter in letters:
                    palindrome = first_half + letter + first_half[::-1]
                    if palindrome not in palindromes:
                        palindromes.add(palindrome)
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes