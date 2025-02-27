from itertools import combinations
    from collections import Counter

def palindromes_between_indices(s):
    s = s.lower()[1:9]
    counter = Counter(s)
    chars = [char * (count // 2) for char, count in counter.items()]
    half = ''.join(chars)
    palindromes = set()
    for i in range(len(half)):
        for comb in combinations(half, i):
            word = ''.join(comb)
            if len(word) >= 2:
                palindrome = word + word[::-1]
                if all((counter[char] >= 2 for char in set(palindrome))):
                    palindromes.add(palindrome)
    return palindromes