def palindromes_between_indices(some_str):
    palindromes = set()
    for s in some_str[4:10].lower():
        if s.isalpha():
            for p in permutations(s):
                if p not in palindromes and p[:len(p) // 2][::-1] == p[len(p) // 2:]:
                    palindromes.add(p)
    return palindromes