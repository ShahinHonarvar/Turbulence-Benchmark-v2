from collections import Counter
    from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = ''.join(filter(str.isalpha, s[2:10])).lower()
    counter = Counter(substr)
    palindromes = set()
    for length in range(4, len(substr) + 1):
        for comb in combinations(substr, length):
            comb_counter = Counter(comb)
            if all((comb_counter[ch] % 2 == 0 or (comb_counter[ch] == 1 and comb_counter[ch] == counter[ch]) for ch in comb_counter)):
                half = ''.join(sorted(comb[:len(comb) // 2]))
                palindrome = half + half[::-1]
                if is_palindrome(palindrome) and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes