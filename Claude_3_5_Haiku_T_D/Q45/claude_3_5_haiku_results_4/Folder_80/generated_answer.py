from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            for i in range(length // 2 + 1):
                if ''.join(perm[i:length - i]) == ''.join(perm[i:length - i])[::-1]:
                    palindrome = ''.join(perm)
                    if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
                    break
    return palindromes