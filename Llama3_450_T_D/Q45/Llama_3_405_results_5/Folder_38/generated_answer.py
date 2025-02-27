import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    letters_set = set(letters)
    if len(letters_set) < 5:
        return set()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes