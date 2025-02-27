def palindromes_between_indices(s):
    string_between_indices = s[8:10]
    palindromes = set()
    for word in string_between_indices.lower():
        for i in range(3, len(string_between_indices) + 1):
            combinations = itertools.permutations(string_between_indices, i)
            for combination in combinations:
                joined_combination = ''.join(combination)
                if joined_combination == joined_combination[::-1]:
                    palindromes.add(joined_combination)
    return palindromes