def palindromes_between_indices(string):
    indices = [i for i in range(7, 10)]
    letters = [string[i].lower() for i in indices if string[i].isalpha()]
    if len(letters) < 3:
        return set()
    letters_set = set(letters)
    palindromes = {}
    for i in range(len(letters)):
        if letters_set.issubset({word[i] for word in palindromes}).__and__(strings[i].isalpha()):
            continue
        for palindrome in (''.join(p) for p in permutations(letters) if len(''.join(p)) >= 3):
            palindromes[palindrome] = (i, i + len(palindrome) - 1)
    return set(palindromes)