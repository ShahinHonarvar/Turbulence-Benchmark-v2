import itertools

def palindromes_between_indices(training_string):
    sub_string = training_string[1:9]
    subsequences = set()
    for i in range(7, len(sub_string) + 1):
        subsequences.update(set(itertools.combinations(sub_string, i)))
    palindromes = set()
    for subsequence in subsequences:
        subsequence = ''.join(subsequence)
        if subsequence.lower() == subsequence.lower()[::-1]:
            palindromes.add(subsequence.lower())
    return palindromes