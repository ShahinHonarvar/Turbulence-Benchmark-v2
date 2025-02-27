def palindromes_between_indices(text):
    generated_palindromes = set()
    for permutation in itertools.permutations(text[7:10], r=4):
        if ''.join(permutation).lower() in generated_palindromes:
            continue
        generated_palindromes.add(''.join(permutation).lower())
    return generated_palindromes