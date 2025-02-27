import itertools

def palindromes_between_indices(string):
    string = string[2:5]
    string = string.lower()
    string_set = set(string)
    palindromes = set()
    for i in range(3, len(string) + 1):
        for combination in itertools.combinations(string_set, i):
            combination = ''.join(combination)
            for palindrome in itertools.permutations(combination):
                palindrome = ''.join(palindrome)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes