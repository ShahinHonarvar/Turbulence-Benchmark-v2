def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = set(s[1:8].lower())
    potential_palindromes = set()
    for length in range(6, len(s) + 1):
        for palindrome in [''.join(p) for p in permutations(chars, length)]:
            if is_palindrome(palindrome):
                potential_palindromes.add(palindrome)
    return potential_palindromes