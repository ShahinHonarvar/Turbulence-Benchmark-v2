import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:4] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes