from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    letters = defaultdict(int)
    for i in range(3, 10):
        letters[s[i].lower()] += 1
    for length in range(7, len(letters) + 1):
        for comb in itertools.combinations_with_replacement(letters.items(), length):
            palindrome = ''.join(sorted((k * v for k, v in comb)))
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result