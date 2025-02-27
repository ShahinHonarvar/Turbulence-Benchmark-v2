from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    extracted_letters = [char.lower() for char in s[1:7] if char.isalpha()]
    palindromes = set()
    for perm in permutations(extracted_letters):
        sliced = ''.join(perm)
        for size in range(7, len(sliced) + 1):
            for i in range(0, len(sliced) - size + 1):
                possible_palindrome = sliced[i:i + size]
                if is_palindrome(possible_palindrome):
                    palindromes.add(possible_palindrome)
    return palindromes