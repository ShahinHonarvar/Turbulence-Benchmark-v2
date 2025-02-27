def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def all_permutations(s):
        if len(s) == 1:
            return [s]
        else:
            permutations = []
            for p in all_permutations(s[1:]):
                for i in range(len(p) + 1):
                    permutations.append(p[:i] + s[0:1] + p[i:])
            return permutations
    s = s[3:9]
    permutations = all_permutations(s)
    palindromes = set()
    for p in permutations:
        if is_palindrome(p) and len(p) >= 3:
            palindromes.add(p)
    if len(palindromes) == 0:
        return set()
    else:
        return palindromes