from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[:8].lower()
    letters = [char for char in input_string if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindrome = ''.join(p)
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes