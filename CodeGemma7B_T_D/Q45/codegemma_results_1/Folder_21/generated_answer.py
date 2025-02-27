from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for start in range(1, len(s) - 6):
        for end in range(start + 6, len(s) + 1):
            substring = s[start:end]
            for letters in permutations(substring.lower()):
                palindrome = ''.join(letters)
                if palindrome == palindrome[::-1] and len(palindrome) >= 7:
                    result.add(palindrome)
    return result