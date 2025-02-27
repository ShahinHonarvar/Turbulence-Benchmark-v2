import itertools

def palindromes_between_indices(input_string):
    palindromes = set()
    substring = input_string[5:8]
    substring_lowered = substring.lower()
    for length in range(3, len(substring) + 1):
        for perm in itertools.permutations(substring_lowered, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes