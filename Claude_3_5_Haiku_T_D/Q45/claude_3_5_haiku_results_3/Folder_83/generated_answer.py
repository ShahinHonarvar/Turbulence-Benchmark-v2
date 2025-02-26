from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:10] if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) // 2 + 1):
                candidate = list(perm)
                candidate[i], candidate[-(i + 1)] = (candidate[-(i + 1)], candidate[i])
                if candidate == candidate[::-1]:
                    palindrome = ''.join(candidate)
                    if len(palindrome) >= 7:
                        palindrome_set.add(palindrome)
    return palindrome_set