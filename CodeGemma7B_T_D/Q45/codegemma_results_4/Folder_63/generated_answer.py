def palindromes_between_indices(text: str) -> set[str]:
    lowercase_text = text.lower()
    unique_letters = set(lowercase_text[0:4])
    palindromes = set()
    for permutation in itertools.permutations(unique_letters):
        palindrome = ''.join(permutation)
        if palindrome in lowercase_text[0:4]:
            palindromes.add(palindrome)
    return palindromes