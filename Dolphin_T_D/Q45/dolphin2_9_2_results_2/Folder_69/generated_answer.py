def palindromes_between_indices(s):
    set_s = set(s.lower())
    palindromes = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    palindromes = palindromes.intersection(set_s)
    return palindromes