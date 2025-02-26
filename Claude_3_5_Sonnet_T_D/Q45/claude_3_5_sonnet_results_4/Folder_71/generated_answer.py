from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[1:4])).lower()
    if len(letters) < 2:
        return set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, min_length=4):
        palindromes = set()
        for i in range(min_length, len(chars) * 2 + 1):
            for perm in permutations(chars, i // 2):
                half = ''.join(perm)
                if i % 2 == 0:
                    palindrome = half + half[::-1]
                else:
                    palindrome = half + half[-1] + half[::-1]
                if len(palindrome) >= min_length and is_palindrome(palindrome):
                    palindromes.add(palindrome)
        return palindromes
    return generate_palindromes(letters)