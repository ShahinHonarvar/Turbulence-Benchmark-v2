import itertools

def palindromes_between_indices(string):
    substring = string.lower()[0:5]
    palindromes = set()
    for i in range(3, len(substring)):
        for palindrome in itertools.permutations(substring, i):
            if palindrome == palindrome[::-1]:
                palindrome_word = ''.join(palindrome)
                palindromes.add(palindrome_word)
    return palindromes