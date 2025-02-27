def palindromes_between_indices(s):

    def palindrome(s):
        return s == s[::-1]

    def all_permutations(s):
        if len(s) == 1:
            return set(s)
        else:
            perms = all_permutations(''.join(s[1:]))
            uniq_perms = set()
            for p in perms:
                for i in range(len(p) + 1):
                    uniq_perms.add(p[:i] + s[0] + p[i:])
        return uniq_perms
    str_slice = s[4:10]
    str_slice_palindromes = set(filter(palindrome, map(str.lower, all_permutations(str_slice))))
    return str_slice_palindromes