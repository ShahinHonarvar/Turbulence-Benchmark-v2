def palindromes_between_indices(string):
    filtered_string = ''.join((char for char in string[2:9] if char.isalpha()))
    filtered_string = filtered_string.lower()
    palindromes = set()
    permutations = set(itertools.permutations(filtered_string))
    for perm in permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes