import itertools
    from collections import Counter

def palindromes_between_indices(input_string):
    substring = input_string[3:10]
    substring = substring.lower()
    char_counter = Counter(substring)
    palindrome_set = set()
    for perm_length in range(5, len(substring) + 1):
        for perm in itertools.permutations(substring, perm_length):
            if perm == perm[::-1]:
                if all((char_counter[char] >= perm.count(char) for char in perm)):
                    palindrome_set.add(''.join(perm))
    return palindrome_set