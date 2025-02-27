import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[:9])).lower()
    letters = list(substring)
    palindromes = set()
    for length in range(7, len(substring) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes