from itertools import product

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in product(letters_set, repeat=length // 2):
            palindrome = ''.join(p + p[::-1])
            if length % 2 == 1:
                for c in letters_set:
                    palindrome = palindrome[:-1] + c + palindrome[-1]
                    palindromes.add(palindrome)
                    palindrome = palindrome[:-2] + c + palindrome[-1:]
            else:
                palindromes.add(palindrome)
    return palindromes