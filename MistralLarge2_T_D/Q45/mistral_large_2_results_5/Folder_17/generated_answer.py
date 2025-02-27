import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    filtered_chars = [char.lower() for char in s[2:7] if char.isalpha()]
    palindromes = set()
    for length in range(4, len(filtered_chars) + 1):
        for comb in itertools.permutations(filtered_chars, length):
            word = ''.join(comb)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes