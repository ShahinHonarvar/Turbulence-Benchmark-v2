import itertools

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(27, len(s) + 1):
        for combination in itertools.combinations(s, length):
            palindrome = ''.join(combination)
            if all((letter in alphabet for letter in palindrome)):
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes