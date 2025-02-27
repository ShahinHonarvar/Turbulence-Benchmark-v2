from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for p in permutations(s):
        for i in range(1, len(p) + 1):
            for j in range(len(p) - i + 1):
                sub_palindrome = ''.join(p[j:j + i])
                if sub_palindrome == sub_palindrome[::-1] and len(sub_palindrome) >= 7:
                    palindromes.add(sub_palindrome)
    return palindromes