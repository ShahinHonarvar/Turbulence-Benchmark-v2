import itertools

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[3:6]))
    substring = substring.lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for combination in itertools.combinations_with_replacement(substring, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes