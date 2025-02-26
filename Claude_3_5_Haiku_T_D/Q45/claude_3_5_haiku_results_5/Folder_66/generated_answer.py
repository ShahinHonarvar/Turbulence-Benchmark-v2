from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:6] if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            for start in range(length - length // 2 + 1):
                candidate = list(perm[start:start + length // 2])
                remaining = list(perm[length // 2:])
                remaining.reverse()
                if length % 2 == 1:
                    pivot = perm[length // 2]
                    candidate.append(pivot)
                candidate.extend(remaining)
                palindrome = ''.join(candidate)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes