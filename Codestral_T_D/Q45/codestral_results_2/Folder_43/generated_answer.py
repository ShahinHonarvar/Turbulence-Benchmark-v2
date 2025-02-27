import itertools

def palindromes_between_indices(input_string):
    input_string = input_string[2:6].lower()
    palindromes = set()
    for length in range(4, len(input_string) + 1):
        for perm in itertools.permutations(input_string, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes