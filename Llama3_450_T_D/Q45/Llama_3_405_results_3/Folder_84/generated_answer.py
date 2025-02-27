from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    target_string = ''.join(filter(str.isalpha, s[4:10])).lower()
    unique_letters = ''.join(set(target_string))
    palindromes = set()
    for r in range(3, len(target_string) + 1):
        for perm in permutations(unique_letters, r):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                if all((palindrome.count(c) <= target_string.count(c) for c in palindrome)):
                    palindromes.add(palindrome)
    return palindromes