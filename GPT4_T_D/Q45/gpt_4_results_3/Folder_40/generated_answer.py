from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:10].lower()
    palindromes = set()
    for i in range(7, len(sub_string) + 1):
        perm = permutations(sub_string, i)
        for j in list(perm):
            temp_str = ''.join(j)
            if temp_str == temp_str[::-1]:
                palindromes.add(temp_str)
    return palindromes