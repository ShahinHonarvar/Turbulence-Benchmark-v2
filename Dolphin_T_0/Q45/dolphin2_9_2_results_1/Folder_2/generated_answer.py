import itertools

def palindromes_between_indices(s):
    index_1_to_5 = s[1:6]
    palindromes_set = set()
    for length in range(6, len(index_1_to_5) + 1):
        for combination in itertools.combinations(index_1_to_5, length):
            palindrome = ''.join(combination)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes_set.add(palindrome)
    return palindromes_set