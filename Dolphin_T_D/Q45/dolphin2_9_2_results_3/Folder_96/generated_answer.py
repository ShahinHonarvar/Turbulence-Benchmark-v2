from string import ascii_letters as letters

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    s = s[3:9].lower()
    english_letters = {char for char in s if char in letters}
    palindromes = set()
    if len(english_letters) >= 6:
        for length in range(6, len(english_letters) + 1):
            for combination in itertools.combinations(english_letters, length):
                word = ''.join(combination)
                for permutation in set(itertools.permutations(word)):
                    if is_palindrome(''.join(permutation)):
                        palindromes.add(permutation)
    return palindromes