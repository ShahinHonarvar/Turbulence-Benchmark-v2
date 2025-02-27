def palindromes_between_indices(str_input):
    substring = str_input[2:5]
    palindromes_set = set()

    def is_palindrome(test_string):
        return test_string == test_string[::-1]
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            combination = substring[i:j]
            if len(combination) < 4:
                continue
            for permutation in set(map(''.join, itertools.permutations(combination))):
                if is_palindrome(permutation) and len(permutation) >= 4:
                    palindromes_set.add(permutation.lower())
    return palindromes_set