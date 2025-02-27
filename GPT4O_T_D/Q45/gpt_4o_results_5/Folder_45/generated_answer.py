from itertools import permutations

def palindromes_between_indices(input_string):
    if len(input_string) < 10:
        return set()
    relevant_letters = [c.lower() for c in input_string[5:10] if c.isalpha()]
    if not relevant_letters:
        return set()
    palindromes = set()
    for perm in permutations(relevant_letters):
        if any((perm[i] != perm[-i - 1] for i in range(2))):
            continue
        palindrome_candidate = ''.join(perm)
        if len(palindrome_candidate) >= 4:
            if palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes