from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:6] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            if len(candidate) % 2 == 0:
                mid = len(candidate) // 2
                left = candidate[:mid]
                right = candidate[mid:]
                right.reverse()
                if left == right and len(left) >= 2:
                    palindrome_set.add(''.join(candidate))
            else:
                mid = len(candidate) // 2
                left = candidate[:mid]
                right = candidate[mid + 1:]
                center = candidate[mid]
                right.reverse()
                if left == right and len(left) >= 2:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set