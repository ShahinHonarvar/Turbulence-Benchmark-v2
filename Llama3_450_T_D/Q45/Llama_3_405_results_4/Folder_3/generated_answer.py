import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[7:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(unique_letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes