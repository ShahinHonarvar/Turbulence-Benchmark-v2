import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[6:10].lower() if c.isalpha()]
    letters_set = set(letters)
    if len(letters_set) < 2:
        return set()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters_set, r // 2):
            first_half = ''.join(combination)
            if r % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                for letter in letters_set:
                    palindrome = first_half + letter + first_half[::-1]
                    if len(palindrome) >= 5:
                        palindromes.add(palindrome)
    return palindromes