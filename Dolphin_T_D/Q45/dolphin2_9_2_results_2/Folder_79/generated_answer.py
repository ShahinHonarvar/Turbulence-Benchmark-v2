from itertools import permutations
	from string import ascii_letters

def palindromes_between_indices(s):
    palindrome_set = set()
    sub_str = ''
    for i in range(1, 8):
        if s[i] in ascii_letters:
            sub_str += s[i].lower()
    if len(set(sub_str)) < 3:
        return palindrome_set
    for p in range(3, len(sub_str) + 1):
        for subset in permutations(sub_str, p):
            test_str = ''.join(subset)
            test_str_rev = test_str[::-1]
            if test_str == test_str_rev:
                palindrome_set.add(test_str.lower())
    return palindrome_set