from collections import defaultdict

def palindromes_between_indices(s):
    palindromes = set()
    letters = defaultdict(list)
    n = min(8, len(s))
    for i in range(n):
        for j in range(i, n):
            letter_combination = tuple((s[k].lower() for k in range(i, j + 1)))
            for comb in itertools.permutations(letter_combination):
                if letters[comb]:
                    palindrome = ''.join(comb)
                    palindromes.add(palindrome)
                else:
                    letters[comb] = True
    return palindromes