import re

def palindromes_between_indices(s):
    eng_letters = set(re.findall('[a-zA-Z]', s[1:4]))
    palindromes = {palindrome for length in range(4, len(eng_letters) + 1) for i in range(len(eng_letters) - length + 1) for permutation in itertools.permutations(eng_letters, length) for palindrome in (''.join(permutation), ''.join(permutation)[::-1]) if palindrome == palindrome.lower()}
    return palindromes