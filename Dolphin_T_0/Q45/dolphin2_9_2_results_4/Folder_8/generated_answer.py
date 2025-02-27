import itertools

def palindromes_between_indices(s):
    sub_s = s[1:6]
    palindromes = set()
    for i in range(5, 0, -1):
        for combination in itertools.combinations(sub_s, i):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome.lower())
    return palindromes