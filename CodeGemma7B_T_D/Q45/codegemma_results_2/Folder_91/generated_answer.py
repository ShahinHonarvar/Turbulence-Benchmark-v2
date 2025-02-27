def palindromes_between_indices(input_str):
    valid_runes = set((letters.lower() for letters in input_str[2:7]))
    result = set()
    for perm in permutations(valid_runes):
        palindrome = ''.join(perm)
        if all((letter in perm for letter in palindrome)):
            result.add(palindrome)
    return result