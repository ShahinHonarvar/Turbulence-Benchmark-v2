import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:8].lower()))
    letters = sorted(set(s))
    palindromes = set()
    for length in range(4, len(s) + 1):
        for combination in itertools.combinations_with_replacement(letters, length // 2):
            palindrome = ''.join(combination) + ''.join(combination[::-1])
            if len(palindrome) == length and palindrome in s:
                palindromes.add(palindrome)
            if length % 2:
                for letter in letters:
                    palindrome = ''.join(combination) + letter + ''.join(combination[::-1])
                    if palindrome in s:
                        palindromes.add(palindrome)
    return palindromes