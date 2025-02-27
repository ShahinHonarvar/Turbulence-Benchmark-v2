def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(5) if s[i].isalpha()))
    palindromes = {p for length in range(4, 1, -1) for p in list(itertools.product(letters, repeat=length))}
    palindromes = {p for p in palindromes if p[::-1] == p}
    palindromes = {p for p in palindromes if all((c in p for c in ('a', 'e', 'i', 'o', 'u')))}
    return palindromes