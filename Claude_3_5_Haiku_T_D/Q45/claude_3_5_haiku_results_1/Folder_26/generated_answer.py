import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:7] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for arrangement in itertools.permutations(letters, length):
            for palindrome in itertools.permutations(arrangement):
                if list(palindrome) == list(palindrome)[::-1]:
                    palindromes.add(''.join(palindrome))
    return palindromes