from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    segment = s[1:7].lower()
    segment_letters = [ch for ch in segment if ch.isalpha()]
    perms = set(permutations(segment_letters))
    possible_palindromes = set()
    for perm in perms:
        joined_perm = ''.join(perm)
        for i in range(len(joined_perm) // 2 + 1):
            prefix = joined_perm[:i]
            palindrome_candidate = prefix + joined_perm[i:len(joined_perm) - i][::-1] + prefix[::-1]
            if len(palindrome_candidate) >= 7 and palindrome_candidate == palindrome_candidate[::-1]:
                possible_palindromes.add(palindrome_candidate)
    return possible_palindromes